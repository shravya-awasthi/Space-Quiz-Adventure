# Tests for the Space Quiz project
# These check the questions, the score file and the helper functions.
# The Tkinter window itself is tested by hand (see docs/testing.md).
#
# How to run (from the project folder):
#   python -m unittest test_quiz -v

import os
import tempfile
import unittest

from questions import LEVELS
from score import save_score, get_scores
from utils import get_ascii_ship, clamp


class TestQuestions(unittest.TestCase):

    def test_there_are_three_levels(self):
        self.assertEqual(len(LEVELS), 3)
        self.assertIn(1, LEVELS)
        self.assertIn(2, LEVELS)
        self.assertIn(3, LEVELS)

    def test_each_level_has_five_questions(self):
        for level in LEVELS:
            self.assertEqual(len(LEVELS[level]), 5)

    def test_each_question_has_all_keys(self):
        for level in LEVELS:
            for q in LEVELS[level]:
                self.assertIn("question", q)
                self.assertIn("options", q)
                self.assertIn("answer", q)

    def test_each_question_has_four_options(self):
        # the game makes exactly 4 answer buttons
        for level in LEVELS:
            for q in LEVELS[level]:
                self.assertEqual(len(q["options"]), 4)

    def test_answer_index_is_valid(self):
        # answer must be 0, 1, 2 or 3
        for level in LEVELS:
            for q in LEVELS[level]:
                self.assertTrue(q["answer"] >= 0)
                self.assertTrue(q["answer"] < len(q["options"]))

    def test_question_text_is_not_empty(self):
        for level in LEVELS:
            for q in LEVELS[level]:
                self.assertTrue(q["question"].strip() != "")

    def test_options_are_not_repeated(self):
        for level in LEVELS:
            for q in LEVELS[level]:
                self.assertEqual(len(set(q["options"])), len(q["options"]))


class TestScore(unittest.TestCase):

    def setUp(self):
        # work inside a temp folder so the real scores.txt is not touched
        self.old_folder = os.getcwd()
        self.temp_folder = tempfile.mkdtemp()
        os.chdir(self.temp_folder)

    def tearDown(self):
        os.chdir(self.old_folder)
        path = os.path.join(self.temp_folder, "scores.txt")
        if os.path.exists(path):
            os.remove(path)
        os.rmdir(self.temp_folder)

    def test_no_file_gives_empty_list(self):
        # get_scores should not crash if scores.txt is missing
        self.assertEqual(get_scores(), [])

    def test_save_one_score(self):
        save_score("Riya", 30)
        lines = get_scores()
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0], "Riya - 30\n")

    def test_scores_are_added_not_replaced(self):
        save_score("Riya", 30)
        save_score("Arjun", 50)
        lines = get_scores()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], "Riya - 30\n")
        self.assertEqual(lines[1], "Arjun - 50\n")

    def test_zero_score_is_saved(self):
        save_score("Sam", 0)
        self.assertEqual(get_scores()[0], "Sam - 0\n")

    def test_name_with_space_and_accent(self):
        save_score("Zoë Lee", 20)
        self.assertEqual(get_scores()[0], "Zoë Lee - 20\n")


class TestUtils(unittest.TestCase):

    def test_ship_is_a_string(self):
        ship = get_ascii_ship()
        self.assertIsInstance(ship, str)
        self.assertTrue(len(ship) > 0)

    def test_ship_has_nasa_and_space_text(self):
        ship = get_ascii_ship()
        self.assertIn("NASA", ship)
        self.assertIn("SPACE", ship)

    def test_clamp_value_inside_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_clamp_value_too_small(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_clamp_value_too_big(self):
        self.assertEqual(clamp(42, 0, 10), 10)

    def test_clamp_on_the_edges(self):
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)


if __name__ == "__main__":
    unittest.main()
