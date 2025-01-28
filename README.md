# League Ranking CLI Application

## Overview

This is a command-line application that calculates the ranking table for a football league based on match results. The application processes match results, assigns points based on the outcome, and ranks teams accordingly.

## Features

- Reads match results from a file or standard input.
- Calculates points based on wins, draws, and losses.
- Sorts teams by points (highest to lowest) and handles ties alphabetically.
- Provides a formatted ranking table as output.
- Includes unit tests.

## How to Run the Application

### Using a File as Input

Run the following command to process match results from a file:

```sh
python main.py input.txt
```

### Using Standard Input

If you prefer entering match results manually, run:

```sh
python main.py
```

Then, enter match results line by line, and type `END` and press `ENTER` to finish input.

## Expected Input Format

Each line should contain match results in the following format:

```
TeamA ScoreA, TeamB ScoreB
```

Example:

```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
```

## Expected Output Format

The application outputs the league standings in the following format:

```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

## How to Run Tests

This project includes a test suite to verify functionality. To run the tests, execute:

```sh
python -m unittest test_main.py
```

## Error Handling

- Matches where a team plays against itself are ignored.
- Negative scores are not allowed.
- Non-numeric scores are ignored.
- Invalid lines are skipped with an error message.

## Dependencies

- No external libraries are required.
