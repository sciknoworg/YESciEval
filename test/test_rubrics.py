import unittest
from yescieval import Informativeness

class TestRubric(unittest.TestCase):

    def setUp(self):
        self.papers = {
            "A Study on AI": "This paper discusses recent advances in AI.",
            "Machine Learning Basics": "An overview of supervised learning methods."
        }
        self.question = "this is a dume question"
        self.answer = "synthesis answer"

    def test_informativeness(self):
        rubric = Informativeness(papers=self.papers, question=self.question, answer=self.answer)
        output = rubric.instruct()
        self.assertIsInstance(output, list)
        self.assertTrue(len(output) > 0)

if __name__ == '__main__':
    unittest.main()
