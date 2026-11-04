import unittest
from pydantic import ValidationError
from yescieval import ExampleInjector, Rubric, VocabularyInjector
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

class MinimalRubric(Rubric):
    """Test rubric inheriting directly from `Rubric` with no synthesis inputs."""

    system_prompt_template: str = "You are a test judge."
    user_prompt_template: str = "Evaluate: {text}"
    text: str

    def verbalize_user_prompt(self) -> str:
        return self.user_prompt_template.format(text=self.text)


class TestRubricHierarchy(unittest.TestCase):

    def setUp(self):
        self.papers = {
            "Paper One": "Abstract one.",
            "Paper Two": "Abstract two.",
        }
        self.question = "What is studied?"
        self.rendered_papers = "1. Paper One\n\nAbstract one.\n\n2. Paper Two\n\nAbstract two.\n\n"

    def test_base_rubric_has_no_synthesis_fields(self):
        self.assertNotIn("papers", Rubric.model_fields)
        self.assertNotIn("question", Rubric.model_fields)

    def test_minimal_rubric_without_papers_or_question(self):
        rubric = MinimalRubric(text="some evidence")
        self.assertEqual(rubric.instruct(), [
            {"role": "system", "content": "You are a test judge."},
            {"role": "user", "content": "Evaluate: some evidence"},
        ])

    def test_pointwise_requires_papers_and_question(self):
        for missing in ("papers", "question"):
            kwargs = {"papers": self.papers, "question": self.question, "answer": "ans"}
            del kwargs[missing]
            with self.assertRaises(ValidationError):
                Informativeness(**kwargs)

    def test_pairwise_requires_papers_and_question(self):
        for missing in ("papers", "question"):
            kwargs = {"papers": self.papers, "question": self.question, "answer_a": "a", "answer_b": "b"}
            del kwargs[missing]
            with self.assertRaises(ValidationError):
                MethodCoverage(**kwargs)

    def test_pointwise_user_prompt_unchanged(self):
        rubric = Informativeness(papers=self.papers, question=self.question, answer="ans")
        self.assertEqual(rubric.render_papers(), self.rendered_papers)
        self.assertEqual(rubric.instruct()[1]["content"], (
            "Evaluate and rate the quality of the following scientific synthesis "
            "according to the characteristics given in the system prompt.\n"
            "\n<scientific-synthesis>\nans\n</scientific-synthesis>\n"
            "\n<research-question>\nWhat is studied?\n</research-question>\n"
            f"\n<paper-titles-and-abstracts>\n{self.rendered_papers}\n</paper-titles-and-abstracts>\n\n###"
        ))

    def test_pairwise_user_prompt_unchanged(self):
        rubric = MethodCoverage(papers=self.papers, question=self.question, answer_a="a", answer_b="b")
        self.assertEqual(rubric.render_papers(), self.rendered_papers)
        self.assertEqual(rubric.instruct()[1]["content"], (
            "Evaluate and rate the quality of the following scientific synthesis "
            "according to the characteristics given in the system prompt.\n"
            "\n<scientific-synthesis-A>\na\n</scientific-synthesis-A>\n"
            "\n<scientific-synthesis-B>\nb\n</scientific-synthesis-B>\n"
            "\n<research-question>\nWhat is studied?\n</research-question>\n"
            f"\n<paper-titles-and-abstracts>\n{self.rendered_papers}\n</paper-titles-and-abstracts>\n\n###"
        ))


if __name__ == '__main__':
    unittest.main()
