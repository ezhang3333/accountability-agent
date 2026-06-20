import time

from process_tracker import is_process_running, close_process_by_name
from constants import DEFAULT_ROCKET_LEAGUE_TIMEOUT_INTERVAL, ROCKET_LEAGUE_PROCESS_NAME

PLAY_SESSION_SECONDS = 60 * 60


def ask_for_positive_float(prompt: str, default_value: float) -> float:
    """
    Ask for a positive number. Blank input uses the provided default.
    """
    while True:
        user_input = input(f"{prompt} [{default_value}]: ").strip()

        if user_input == "":
            return default_value

        try:
            value = float(user_input)
        except ValueError:
            print("Please enter a number.")
            continue

        if value <= 0:
            print("Please enter a number greater than 0.")
            continue

        return value


def launch_accountability_app(
    play_session_seconds: float,
    check_interval_seconds: float,
) -> None:
    """
    Monitor Rocket League and close it after the allowed play session ends.
    """
    play_session_end_time = None

    print("Accountability app started. Press Ctrl+C to stop.")

    while True:
        current_time = time.time()
        rocket_league_running = is_process_running(ROCKET_LEAGUE_PROCESS_NAME)

        if rocket_league_running:
            if play_session_end_time is None:
                play_session_end_time = current_time + play_session_seconds
                print("Rocket League session started.")

            elif current_time >= play_session_end_time:
                close_process_by_name(ROCKET_LEAGUE_PROCESS_NAME)
                play_session_end_time = None
                print("Rocket League session ended.")
        else:
            play_session_end_time = None

        time.sleep(check_interval_seconds)


def launch_accoutability_app() -> None:
    """
    Backward-compatible wrapper for the old misspelled function name.
    """
    launch_accountability_app(PLAY_SESSION_SECONDS, DEFAULT_ROCKET_LEAGUE_TIMEOUT_INTERVAL)


def main() -> None:
    """
    Bare-bones command-line setup for the accountability app.
    """
    print("Rocket League Accountability App")
    check_interval_seconds = ask_for_positive_float(
        "How often should the app check for Rocket League, in seconds?",
        DEFAULT_ROCKET_LEAGUE_TIMEOUT_INTERVAL,
    )
    play_session_minutes = ask_for_positive_float(
        "How many minutes should Rocket League be allowed to run?",
        PLAY_SESSION_SECONDS / 60,
    )

    launch_accountability_app(
        play_session_seconds=play_session_minutes * 60,
        check_interval_seconds=check_interval_seconds,
    )


if __name__ == "__main__":
    main()
