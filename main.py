import time
import tkinter as tk

from process_tracker import is_process_running, close_process_by_name
from constants import DEFAULT_ROCKET_LEAGUE_TIMEOUT_INTERVAL, ROCKET_LEAGUE_PROCESS_NAME, DEFAULT_ROCKET_LEAGUE_ALLOCATED_PLAY_TIME

PLAY_SESSION_SECONDS = 60 * 60

root = tk.Tk()

root.title("STOP PLAYING ROCKET LEAGUE")
root.geometry("300x150")

label = tk.Label(root, text="Rocket League DETECTED")
label.pack(pady=20)

button = tk.Button(root, text="OK", command=root.quit)
button.pack()

def launch_accountabilty_app() -> None:
    eligible_for_timeout = False

    while is_process_running(ROCKET_LEAGUE_PROCESS_NAME):
        if eligible_for_timeout:
            close_process_by_name(ROCKET_LEAGUE_PROCESS_NAME)
            root.deiconify()
            root.mainloop()
            root.withdraw()

            time.sleep(DEFAULT_ROCKET_LEAGUE_TIMEOUT_INTERVAL)
            eligible_for_timeout = False
        else:
            time.sleep(DEFAULT_ROCKET_LEAGUE_ALLOCATED_PLAY_TIME)
            eligible_for_timeout = True