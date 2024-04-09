from tqdm import tqdm
import time
from datetime import datetime, timedelta
import argparse
import colorama
import subprocess


def pomodoro_segment(name: str, minutes: int):
    print(colorama.Fore.GREEN + f"Time to start {name}")
    
    # Notifications do not work on windows, 
    # I simply try-excepted them, because I did not have time to think for a good solution
    try:
        subprocess.Popen(["notify-send", "Pomodoro", f"Time to start {name}"])
    except:
        pass

    input(colorama.Fore.GREEN + "Press Enter, when ready:" + colorama.Style.RESET_ALL)

    start = time.time()
    start_dt = datetime.strptime(time.ctime(start), "%a %b %d %H:%M:%S %Y")
    end_dt = start_dt + timedelta(minutes = minutes)
    strftime_format = "%H:%M:%S"
    print(f"Start: {start_dt.strftime(strftime_format)}")
    print(f"End: {end_dt.strftime(strftime_format)}")

    elapsed = 0
    with tqdm(total = minutes * 60, 
              bar_format="{desc}: {elapsed} |{bar}| :{percentage:3.0f}%",
              desc=f"{name}", 
              ascii=" #") as pbar:
        while (elapsed < minutes * 60):
            elapsed = time.time() - start
            pbar.update(elapsed - pbar.n)
    print(f"{name} finished!")
    print()


def run_loop(config):
    # Run pomodoro loop
    print("pomodoro".center(config.terminal_columns, "_"))
    print(f"There is {config.n_focus} {config.focus_time}-minute focus segments...".center(config.terminal_columns, " "))
    print(f"And {config.n_focus - 1} {config.small_break_time}-minute small breaks...".center(config.terminal_columns, " "))
    print(f"Cycle finishes with {config.long_break_time}-minute long break".center(config.terminal_columns, " "))
    print("".center(config.terminal_columns, "-"))
    
    cycle_i = 1
    focus_counter = 0
    try:
        while True:
            print(f"Starting cycle {cycle_i}".center(config.terminal_columns, " "))
            print("".center(config.terminal_columns, "-"))

            for focus_segment in range(1, config.n_focus + 1):
                pomodoro_segment(f"Focus ({focus_segment}/{config.n_focus})", config.focus_time)
                focus_counter += 1
                
                if (focus_segment) < config.n_focus:
                    pomodoro_segment("Small Break", config.small_break_time)
                else:
                    pomodoro_segment("Long Break", config.long_break_time)
            cycle_i += 1
    except KeyboardInterrupt:
        print()
        print(colorama.Fore.RED + "Received Ctrl-C, exiting" + colorama.Style.RESET_ALL)
        print()
        print("".center(config.terminal_columns, "-"))
        print("Current run stats")
        print("".center(config.terminal_columns, "-"))
        print(f"Finished cycles: {cycle_i - 1}")
        print(f"Focus segments: {focus_counter}")
