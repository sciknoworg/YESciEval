"""
Minimal end-to-end RoB 2 assessment, without a model or API key.

Run from the repository root:

    python -m examples.rob2_minimal

One fictional trial result with two evidence documents goes through the whole
pipeline: 22 signalling-question rubrics -> judge -> five domain judgments ->
overall judgment. `FakeJudge` answers from a fixed table; it does not read the
documents and does not assess clinical evidence.

To use a real model instead, pass a GPTCustomAutoJudge (no other change):

    import os
    from yescieval import GPTCustomAutoJudge
    from examples.rob2_minimal import make_input, run

    judge = GPTCustomAutoJudge()  # defaults: max_attempts=3, retry_delay=5
    judge.from_pretrained(model_id="gpt-4o-mini", token=os.environ["OPENAI_API_KEY"])
    print(run(make_input(), judge).model_dump_json(indent=2))
"""

from yescieval.base import EvidenceDocument, Judge, RoB2EvaluationInput, RoB2OverallResult, RoB2Rubric
from yescieval.rubric.pointwise.rob2 import RoB2AssessmentRunner

REPORT = """Fictional trial of drug A versus placebo for chronic knee pain.
Participants were randomized 1:1 using a computer-generated random sequence.
Allocation was concealed by a central web-based randomization service.
Baseline characteristics were similar between the two groups.
Participants were blinded using identical-looking placebo tablets.
Care providers were unaware of group assignment throughout the trial.
All randomized participants were analysed in the group to which they were assigned.
Pain scores at 12 weeks were available for 182 of 200 participants (91%).
Missing data were handled by complete-case analysis; no sensitivity analysis was reported.
The most common reason for dropout was lack of pain relief.
Dropout rates and reasons for dropout were similar in both groups.
Pain was measured with the validated WOMAC pain subscale.
The same questionnaire was used at the same visits in both groups.
Participants, who self-reported pain, remained blinded to their assignment."""

SAP = """Statistical analysis plan, version 1.0.
The primary analysis was prespecified in this plan, finalized before unblinding.
The WOMAC pain subscale at 12 weeks is the only prespecified primary outcome measure."""

# rubric_id -> (response, document_id, quote). NI answers carry no evidence.
# Questions not listed here (2.3, 2.4, 2.5, 2.7, 4.4, 4.5) are skipped by the workflow.
ANSWERS = {
    "1.1": ("Y", "report", "computer-generated random sequence"),
    "1.2": ("Y", "report", "concealed by a central web-based randomization service"),
    "1.3": ("N", "report", "Baseline characteristics were similar between the two groups."),
    "2.1": ("N", "report", "Participants were blinded using identical-looking placebo tablets."),
    "2.2": ("N", "report", "Care providers were unaware of group assignment throughout the trial."),
    "2.6": ("Y", "report", "All randomized participants were analysed in the group to which they were assigned."),
    "3.1": ("N", "report", "Pain scores at 12 weeks were available for 182 of 200 participants (91%)."),
    "3.2": ("PN", "report", "no sensitivity analysis was reported"),
    "3.3": ("PY", "report", "The most common reason for dropout was lack of pain relief."),
    "3.4": ("PN", "report", "Dropout rates and reasons for dropout were similar in both groups."),
    "4.1": ("N", "report", "Pain was measured with the validated WOMAC pain subscale."),
    "4.2": ("N", "report", "The same questionnaire was used at the same visits in both groups."),
    "4.3": ("N", "report", "Participants, who self-reported pain, remained blinded to their assignment."),
    "5.1": ("Y", "sap", "The primary analysis was prespecified in this plan, finalized before unblinding."),
    "5.2": ("N", "sap", "The WOMAC pain subscale at 12 weeks is the only prespecified primary outcome measure."),
    "5.3": ("NI", None, None),
}


def make_input() -> RoB2EvaluationInput:
    """One fictional trial result with two evidence documents."""
    return RoB2EvaluationInput(
        study_id="fictional-knee-pain-trial",
        target_outcome="WOMAC pain score, primary analysis",
        intervention="Drug A",
        comparator="Placebo",
        timepoint="12 weeks",
        effect_of_interest="assignment",
        evidence_documents=[
            EvidenceDocument(document_id="report", document_type="primary_report", content=REPORT),
            EvidenceDocument(document_id="sap", document_type="sap", content=SAP),
        ],
    )


class FakeJudge(Judge):
    """
    Answer each signalling question from `ANSWERS`, with no model call.

    Follows the judge contract: returns an instance of `rubric.response_model`,
    validated by the model class and by `rubric.validate_result()`.
    """

    def judge(self, rubric: RoB2Rubric, max_new_tokens: int = 1024):
        response, document_id, quote = ANSWERS[rubric.rubric_id]
        payload = {
            "response": response,
            "rationale": "Fixed answer from the example table.",
            "evidence": [] if response == "NI" else [{"document_id": document_id, "quoted_text": quote}],
        }
        return rubric.validate_result(rubric.response_model.model_validate(payload))


def run(evaluation_input: RoB2EvaluationInput, judge: Judge) -> RoB2OverallResult:
    """Run the complete RoB 2 assessment of one trial result."""
    return RoB2AssessmentRunner().run(evaluation_input, judge)


def print_summary(result: RoB2OverallResult) -> None:
    """Print every signalling answer, the five domain judgments and the overall judgment."""
    for domain_id, domain in result.domains.items():
        print(f"{domain_id}: {domain.suggested_judgment.value}")
        for rubric_id, answer in domain.signaling_results.items():
            print(f"  {rubric_id:<4} {answer.response.value:<3} {answer.rationale}")
    print(f"Overall: {result.suggested_judgment.value}")


if __name__ == "__main__":
    result = run(make_input(), FakeJudge())
    print_summary(result)
    print()
    print(result.model_dump_json(indent=2))
