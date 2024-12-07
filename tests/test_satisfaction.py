import unittest
from algorithms.satisfaction import (
    calculate_candidate_satisfaction,
    calculate_establishment_satisfaction,
    overall_satisfaction
)

class TestSatisfaction(unittest.TestCase):

    def test_calculate_candidate_satisfaction(self):
        preferences = {
            "A": ["X", "Y", "Z"],
            "B": ["Y", "X", "Z"],
            "C": ["Z", "X", "Y"]
        }
        matchings = {"A": "X", "B": "Y", "C": "Z"}
        satisfaction = calculate_candidate_satisfaction(matchings, preferences)
        self.assertAlmostEqual(satisfaction, 1.0)

    def test_calculate_establishment_satisfaction(self):
        preferences = {
            "X": ["A", "B", "C"],
            "Y": ["B", "A", "C"],
            "Z": ["C", "B", "A"]
        }
        matchings = {"A": "X", "B": "Y", "C": "Z"}
        satisfaction = calculate_establishment_satisfaction(matchings, preferences)
        self.assertAlmostEqual(satisfaction, 1.0)

    def test_overall_satisfaction(self):
        candidate_satisfaction = 0.8
        establishment_satisfaction = 0.9
        overall = overall_satisfaction(candidate_satisfaction, establishment_satisfaction, weight=0.6)
        self.assertAlmostEqual(overall, 0.84)

if __name__ == "__main__":
    unittest.main()
