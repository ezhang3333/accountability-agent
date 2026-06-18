from constants import DEFAULT_ROCKET_LEAGUE_TIMEOUT_INTERVAL
import psutil


def is_process_running(process_name: str) -> bool:
    """
    Check whether a process named {process_name} is currently running
    """
    for process_in_check in psutil.process_iter(["name"]):
        try:
            process_in_check_name = process_in_check.info["name"]

            if process_in_check_name is None:
                continue
            if process_in_check_name == process_name:
                return True
        except(psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return False

def close_process(proc: psutil.Process) -> bool:
    """
    Close a process, false being returned means access was denied or process didn't exist
    """
    try:
        proc.terminate()
        proc.wait(timeout=3)
        return True

    except psutil.TimeoutExpired:
        proc.kill()
        return True

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False
    


def close_process_by_name(target_name: str) -> int:
    """
    Closing process by a target process name
    """
    closed_count = 0

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.info["name"] == target_name:
                if close_process(proc):
                    closed_count += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return closed_count