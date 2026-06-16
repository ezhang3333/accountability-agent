from constants import ROCKET_LEAGUE_PROCESS_NAME
import psutil


def is_process_running(process_name: str) -> bool:
    """
    Check whether a process named {process_name} is currently running
    """
    target = process_name.lower()

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
