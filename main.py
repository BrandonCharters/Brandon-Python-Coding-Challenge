import sys


def process_match_results(lines):
    """
    Process the match results and calculate points for each team.

    Parameters:
    lines (list): A list of match results in string format (e.g., "Lions 3, Snakes 3")

    Returns:
    dict: A dictionary with team names as keys and their respective points as values.
    """
    scores = {}  # Dictionary to store team scores

    for line in lines:
        try:
            # Each line contains two teams and their respective scores, separated by ", "
            teams = line.split(", ")

            # Extract team names and scores by splitting at the last space
            team1, score1 = teams[0].rsplit(" ", 1)
            team2, score2 = teams[1].rsplit(" ", 1)

            # Convert score strings into integers
            score1, score2 = int(score1), int(score2)

            # Error Handling: Same team playing against itself
            if team1 == team2:
                raise ValueError(
                    f"Invalid match: A team cannot verse itself ({team1} vs {team2})"
                )

            # Error Handling: Negative scores are not allowed
            if score1 < 0 or score2 < 0:
                raise ValueError(
                    f"Invalid score: Negative scores are not allowed ({team1} {score1}, {team2} {score2})"
                )

            # Initialize team scores in the dictionary if they don't exist
            if team1 not in scores:
                scores[team1] = 0
            if team2 not in scores:
                scores[team2] = 0

            # Assign points based on match results
            if score1 > score2:
                scores[team1] += 3  # Winning team gets 3 points
            elif score2 > score1:
                scores[team2] += 3  # Winning team gets 3 points
            else:
                scores[team1] += 1  # Draw, each team gets 1 point
                scores[team2] += 1

        except ValueError as e:
            print(f"Error processing match result: {e}")
            continue

    return scores  # Return the final scores dictionary


def rank_teams(scores):
    """
    Sort the teams based on points and alphabetical order in case of a tie.

    Parameters:
    scores (dict): Dictionary with team names as keys and points as values.

    Returns:
    list: A sorted list of tuples (team name, points).
    """
    return sorted(
        scores.items(), key=lambda x: (-x[1], x[0])
    )  # Sort by points (desc), then alphabetically


def format_output(ranked_teams):
    """
    Format the ranking table as required.

    Parameters:
    ranked_teams (list): Sorted list of (team name, points).

    Returns:
    str: A formatted string of the ranking table.
    """
    output = []  # List to store the formatted ranking lines
    rank = 0  # Track current rank
    prev_points = None  # Track previous points for rank handling

    for i, (team, points) in enumerate(ranked_teams, start=1):
        if points != prev_points:
            rank = i  # Update rank only if points differ from the last rank

        suffix = "pt" if points == 1 else "pts"  # Handle singular/plural form
        output.append(f"{rank}. {team}, {points} {suffix}")
        prev_points = points  # Update previous points

    return "\n".join(output)  # Convert list to a single string with new lines


def main():
    """
    Main function to read input, process results, rank teams, and print the output.
    """
    if len(sys.argv) > 1:
        # Read input from file if a filename is provided as a command-line argument
        with open(sys.argv[1], "r") as file:
            lines = [line.strip() for line in file.readlines()]
    else:
        # If no filename is given, allow user input through stdin
        print("Enter match results (one per line). Type 'END' to finish:")
        lines = []
        while True:
            line = input().strip()
            if line.lower() == "end":
                break
            lines.append(line)

    scores = process_match_results(lines)  # Process match results to compute scores
    ranked_teams = rank_teams(scores)  # Rank teams based on scores
    print(format_output(ranked_teams))  # Format and print the final ranking table


if __name__ == "__main__":
    main()
