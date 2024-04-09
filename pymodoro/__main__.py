import argparse
from .pomodoro import run_loop
import os
import colorama
from dataclasses import dataclass

############################################################# CONFIG ################################################################
@dataclass
class PomodoroConfig:
    n_focus: int
    focus_time: int
    small_break_time: int
    long_break_time: int
    terminal_columns: int
    silent_flag: bool


# Parse CLI inputs
parser = argparse.ArgumentParser()
parser.add_argument("--n_focus", nargs = "?", default = 4, type = int,
                    help = "Number of focus segments per cycle")
parser.add_argument("--focus_time", nargs = "?", default = 25, type = int,
                    help = "Pomodoro focus time in minutes")
parser.add_argument("--small_break_time", nargs = "?", default = 5, type = int,
                    help = "Pomodoro small break time in minutes")
parser.add_argument("--long_break_time", nargs = "?", default = 15, type = int,
                    help = "Pomodoro long break time in minutes")
parser.add_argument("--silent", action = "store_true")
args = parser.parse_args()

# Determine terminal size for print alignment
terminal_columns = os.get_terminal_size().columns

config = PomodoroConfig(
    n_focus = args.n_focus, 
    focus_time = args.focus_time, 
    small_break_time = args.small_break_time,
    long_break_time = args.long_break_time,
    terminal_columns = terminal_columns,
    silent_flag = args.silent
)

############################################################# RUN ###################################################################
# Run pomodoro loop
run_loop(config)
