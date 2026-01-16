import unittest
from root_agent_selection import RootAgent # Assuming your logic is in this file

class TestAgentSelection(unittest.TestCase):

    def setUp(self):
        # Setup a dummy cluster for testing
        self.mock_cluster = [
            {"name": "HighRated", "tag": [1, 2], "rating": 4.9, "url": "http://test.1"},
            {"name": "LowRated", "tag": [1, 2], "rating": 2.1, "url": "http://test.2"},
            {"name": "Specialist", "tag": [4], "rating": 4.0, "url": "http://test.3"}
        ]
        self.master = RootAgent(self.mock_cluster)

    def test_rating_priority(self):
        """Should pick HighRated (4.9) over LowRated (2.1) for tags {1, 2}"""
        result = self.master.select_best_agent([1, 2])
        self.assertEqual(result['name'], "HighRated")

    def test_specific_tag_selection(self):
        """Should correctly pick the only agent with tag 4"""
        result = self.master.select_best_agent([4])
        self.assertEqual(result['name'], "Specialist")

    def test_no_agent_found(self):
        """Should return None if no agent supports the requested tags"""
        result = self.master.select_best_agent([99]) # Tag 99 doesn't exist
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
