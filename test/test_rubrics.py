import unittest
from yescieval import ExampleInjector, VocabularyInjector
from yescieval.rubric.pointwise.fidelity import Informativeness
from yescieval.rubric.pointwise.depth import CausalReasoning
from yescieval.rubric.pairwise.breadth import MethodCoverage

class TestRubric(unittest.TestCase):

    def setUp(self):
        self.papers = {
            "A Study on AI": "This paper discusses recent advances in AI.",
            "Machine Learning Basics": "An overview of supervised learning methods."
        }
        self.question = "this is a dummy question"
        self.answer = "synthesis answer"

    def test_informativeness(self):
        rubric = Informativeness(papers=self.papers, question=self.question, answer=self.answer)
        output = rubric.instruct()
        self.assertIsInstance(output, list)
        self.assertTrue(len(output) > 0)
        

class TestPointwiseRubric(unittest.TestCase):
 
    def setUp(self):
        self.papers = {
            "A Study on AI": "This paper discusses recent advances in artificial intelligence, including deep learning.",
            "Machine Learning Basics": "An overview of supervised learning methods such as decision trees and SVMs.",
            "Neural Networks Explained": "Explains backpropagation and gradient descent for training networks.",
        }
        self.question = "this is a dummy question"
        self.answer = "synthesis answer"
 
    def test_causal_reasoning(self):
        rubric = CausalReasoning(
            papers=self.papers,
            question=self.question,
            answer=self.answer,
        )
        output = rubric.instruct()
        self.assertIsInstance(output, list)
        self.assertTrue(len(output) > 0)
 
 
class TestPairwiseRubric(unittest.TestCase):

    def setUp(self):
        self.papers = {
            "A Study on AI": "This paper discusses recent advances in artificial intelligence, including deep learning.",
            "Machine Learning Basics": "An overview of supervised learning methods such as decision trees and SVMs.",
            "Neural Networks Explained": "Explains backpropagation and gradient descent for training networks.",
        }
        self.question = "this is a dummy question"
        self.answer_a = "synthesis answer A"
        self.answer_b = "synthesis answer B"

    def test_method_coverage(self):
        rubric = MethodCoverage(
            papers=self.papers,
            question=self.question,
            answer_a=self.answer_a,
            answer_b=self.answer_b,
        )
        output = rubric.instruct()
        self.assertIsInstance(output, list)
        self.assertTrue(len(output) > 0)
        
class TestInjectors(unittest.TestCase):
 
    def setUp(self):
        self.papers = {
            "A Study on AI": "This paper discusses recent advances in artificial intelligence, including deep learning.",
            "Machine Learning Basics": "An overview of supervised learning methods such as decision trees and SVMs.",
            "Neural Networks Explained": "Explains backpropagation and gradient descent for training networks.",
        }
        self.question = "this is a dummy question"
        self.answer_a = "synthesis answer A"
        self.answer_b = "synthesis answer B"
 
    def test_vocabulary_injector(self):
        rubric = MethodCoverage(
            papers=self.papers,
            question=self.question,
            answer_a=self.answer_a,
            answer_b=self.answer_b,
            domain="ecology",
            vocabulary=VocabularyInjector(),
        )
        output = rubric.instruct()
        self.assertIsInstance(output, list)
        self.assertTrue(len(output) > 0)
 
    def test_example_injector(self):
        rubric = MethodCoverage(
            papers=self.papers,
            question=self.question,
            answer_a=self.answer_a,
            answer_b=self.answer_b,
            domain="ecology",
            example=ExampleInjector(),
        )
        output = rubric.instruct()
        self.assertIsInstance(output, list)
        self.assertTrue(len(output) > 0)
 
    def test_both_injectors(self):
        rubric = MethodCoverage(
            papers=self.papers,
            question=self.question,
            answer_a=self.answer_a,
            answer_b=self.answer_b,
            domain="ecology",
            vocabulary=VocabularyInjector(),
            example=ExampleInjector(),
        )
        output = rubric.instruct()
        self.assertIsInstance(output, list)
        self.assertTrue(len(output) > 0)

if __name__ == '__main__':
    unittest.main()
