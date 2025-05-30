from yescieval import Informativeness, AskAutoJudge


papers = {
    "A Study on AI": "This paper discusses recent advances in AI.",
    "Machine Learning Basics": "An overview of supervised learning methods."
}
question = "this is a dume question"
answer="synthesis answer"
rubric = Informativeness(papers=papers, question=question, answer=answer)
inst = rubric.instruct()

judge = AskAutoJudge()

judge.from_pretrained(token="...", device="cpu")


print(judge.evaluate(rubric=rubric))

