from yescieval.rubric import Informativeness


papers = {
    "A Study on AI": "This paper discusses recent advances in AI.",
    "Machine Learning Basics": "An overview of supervised learning methods."
}
question = "this is a dume question"
synthesis="synthesis answer"
rubric = Informativeness(papers=papers, question=question, synthesis=synthesis)
print(rubric.instruct())
