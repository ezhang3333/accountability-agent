import time

from process_tracker import is_process_running, close_process_by_name
from constants import ROCKET_LEAGUE_PROCESS_NAME

PLAY_SESSION_SECONDS = 60 * 60

def launch_accoutability_app() -> None:
    """
    App load initialization process by pulling config variables such as blocked processes, timeout, etc.
    """
    play_session_end_time = None

    while True:
        current_time = time.time()
        rocket_league_running = is_process_running(ROCKET_LEAGUE_PROCESS_NAME)

        if rocket_league_running:
            if play_session_end_time is None:
                play_session_end_time = current_time + PLAY_SESSION_SECONDS
                print("Rocket League session started.")

            elif current_time >= play_session_end_time:
                close_process_by_name(ROCKET_LEAGUE_PROCESS_NAME)
                play_session_end_time = None
                print("Rocket League session ended.")

        time.sleep(1)
 
