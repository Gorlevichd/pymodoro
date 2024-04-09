from tqdm import tqdm
import time
from datetime import datetime, timedelta
import argparse
import colorama


def pomodoro_segment(name: str, minutes: int):
    print(colorama.Fore.GREEN + f"Time to start {name}")
    input(colorama.Fore.GREEN + "Press Enter, when ready:" + colorama.Style.RESET_ALL)

    start = time.time()
    start_dt = datetime.strptime(time.ctime(start), "%a %b %d %H:%M:%S %Y")
    end_dt = start_dt + timedelta(minutes = minutes)
    strftime_format = "%H:%M:%S"
    print(f"Start: {start_dt.strftime(strftime_format)}")
    print(f"End: {end_dt.strftime(strftime_format)}")

    elapsed = 0
    with tqdm(total = minutes * 60, 
              bar_format = "{desc}: {elapsed}|{bar}|:{percentage:3.0f}%",
              desc = f"{name}") as pbar:
        while (elapsed < minutes * 60):
            elapsed = time.time() - start
            pbar.update(elapsed - pbar.n)
    print(f"{name} finished!")
    print("")
