import unittest
from main import process_match_results, rank_teams, format_output


class TestLeagueRanking(unittest.TestCase):
    """
    Test suite for the League Ranking application.
    This includes tests for processing match results, ranking teams, and formatting output.
    """

    def test_process_match_results(self):
        """
        Test the function that processes match results and calculates points for each team.
        """
        test_input = [
            "Lions 3, Snakes 3",  # Draw
            "Tarantulas 1, FC Awesome 0",  # Tarantulas win
            "Lions 1, FC Awesome 1",  # Draw
            "Tarantulas 3, Snakes 1",  # Tarantulas win
            "Lions 4, Grouches 0",  # Lions win
        ]
        expected_output = {
            "Lions": 5,  # 1 win (3 pts) + 2 draws (2 pts) = 5 pts
            "Snakes": 1,  # 1 draw (1 pt) + 1 loss (0 pts) = 1 pt
            "Tarantulas": 6,  # 2 wins (3 pts each) = 6 pts
            "FC Awesome": 1,  # 1 draw (1 pt) + 1 loss (0 pts) = 1 pt
            "Grouches": 0,  # 1 loss (0 pts) = 0 pts
        }
        self.assertEqual(process_match_results(test_input), expected_output)

    def test_rank_teams(self):
        """
        Test the function that ranks teams based on their points and alphabetical order in case of a tie.
        """
        test_scores = {
            "Lions": 5,
            "Snakes": 1,
            "Tarantulas": 6,
            "FC Awesome": 1,
            "Grouches": 0,
        }
        expected_output = [
            ("Tarantulas", 6),  # Highest points
            ("Lions", 5),  # Second highest points
            ("FC Awesome", 1),  # Tie, but comes first alphabetically
            ("Snakes", 1),  # Tie, comes after alphabetically
            ("Grouches", 0),  # Lowest points
        ]
        self.assertEqual(rank_teams(test_scores), expected_output)

    def test_format_output(self):
        """
        Test the function that formats the ranked teams into a readable output.
        """
        test_ranked_teams = [
            ("Tarantulas", 6),
            ("Lions", 5),
            ("FC Awesome", 1),
            ("Snakes", 1),
            ("Grouches", 0),
        ]
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"  # Singular "pt" for 1 point
            "3. Snakes, 1 pt\n"  # Same rank due to tie
            "5. Grouches, 0 pts"
        )
        self.assertEqual(format_output(test_ranked_teams), expected_output)

    def test_invalid_input(self):
        """
        Test that invalid input (negative scores, same team playing itself, non-numeric scores) is handled properly.
        """
        invalid_input = [
            "Lions -1, Snakes 3",  # Negative score, should be ignored
            "Lions 2, Lions 2",  # Same team playing itself, should be ignored
            "Tigers A, Lions 2",  # Non-numeric score, should be ignored
        ]
        self.assertEqual(process_match_results(invalid_input), {})

    def test_empty_input(self):
        """
        Test how the functions handle empty input.
        """
        self.assertEqual(process_match_results([]), {})  # No matches, empty dictionary
        self.assertEqual(rank_teams({}), [])  # No teams, empty list
        self.assertEqual(format_output([]), "")  # No output, empty string


if __name__ == "__main__":
    unittest.main()
