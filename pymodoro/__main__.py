import argparse
from pomodoro import pomodoro_segment

# Parse CLI inputs
parser = argparse.ArgumentParser()
parser.add_argument("--n_cycles", nargs = "?", default = 1, type = int,
                    help = "Number of Pomodoro cycles")
parser.add_argument("--focus", nargs = "?", default = 25, type = int,
                    help = "Pomodoro focus time in minutes")
parser.add_argument("--small_break", nargs = "?", default = 5, type = int,
                    help = "Pomodoro small break time in minutes")
parser.add_argument("--n_focus", nargs = "?", default = 4, type = int,
                    help = "Number of focus segments per cycle")
parser.add_argument("--long_break", nargs = "?", default = 15, type = int,
                    help = "Pomodoro long break time in minutes")
args = parser.parse_args()
    
print("Pomodoro".center(50, "_"))
print("".center(50, "-"))
print(f"Starting pomodoro with {args.n_cycles} cycles")
print(f"There is {args.n_focus} {args.focus}-minute focus segments...")
print(f"And {args.n_focus - 1} {args.small_break}-minute small breaks...")
print(f"Cycle finishes with {args.long_break}-minute long break")
print("".center(50, "-"))

for cycle_i in range(args.n_cycles):
    print(f"Starting cycle {cycle_i}")
    print("".center(50, "-"))

    for focus_segment in range(args.n_focus):
        pomodoro_segment("Focus", args.focus)

        if (focus_segment + 1) < args.n_focus:
            pomodoro_segment("Small Break", args.small_break)
        else:
            pomodoro_segment("Long Break", args.long_break)
