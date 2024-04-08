# pymodoro

## Overview

This is a small project devoted to `Python` CLI realization of a popular time-management technique called Pomodoro.

The idea is simple. By default, there is 1 Pomodoro cycle that contains four 25-minute focus periods, separated by 5-minute short breaks. In general, certain Pomodoro cycle ends with 15-minute large break. Then, the new cycle starts.

## Usage

The package allows to change the default behaviour with flags:

- `--n_cycles` allows to choose the custom number of Pomodoro cycles
- `--focus` allows to specify custom time of focus period in minutes
- `--small_break` allows to specify custom time of small break in minutes
- `--n_focus` allows to specify the amount of focus periods in one cycle
- `--long_break` allows to specify custom time of long break in minutes

For example, 4 cycles of Pomodoro with 50-minute focus periods can be started with:

`python -m pymodoro --n_cycles 4 --focus 50`
