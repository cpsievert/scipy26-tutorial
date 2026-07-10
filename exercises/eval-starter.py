from pathlib import Path

import chatlas as ctl
from pydantic import BaseModel
from inspect_ai import Task, task
from inspect_ai.dataset import json_dataset
from inspect_ai.scorer import model_graded_fact

DATASET_PATH = Path(__file__).parent / "papers_eval.jsonl"


class ModelResult(BaseModel):
    model: str
    dataset: str
    metric: str
    value: float


class PaperResults(BaseModel):
    results: list[ModelResult]


samples = [
    (
        "ResNet-50 achieves 93.2% top-1 accuracy on CIFAR-10 and 76.1% on "
        "ImageNet. A fine-tuned ViT-B/16 reaches 98.1% on CIFAR-10.",
        "Should extract ResNet-50 (93.2% CIFAR-10, 76.1% ImageNet) and "
        "ViT-B/16 (98.1% CIFAR-10).",
    ),
    (
        "GPT-4 scores 86.4% on the MMLU benchmark, while its distilled "
        "variant GPT-4-mini scores 78.9% on the same benchmark.",
        "Should extract GPT-4 (86.4% MMLU) and GPT-4-mini (78.9% MMLU).",
    ),
    (
        "The Segment Anything Model (SAM) achieves a mean IoU of 87.1% on "
        "the COCO segmentation benchmark, compared to 81.3% for the prior "
        "Mask R-CNN baseline.",
        "Should extract SAM (87.1% COCO mIoU) and Mask R-CNN (81.3% COCO mIoU).",
    ),
    (
        "Whisper-large reaches a word error rate of 4.3% on LibriSpeech "
        "test-clean, improving on wav2vec 2.0's 6.1% on the same split.",
        "Should extract Whisper-large (4.3% WER on LibriSpeech test-clean) "
        "and wav2vec 2.0 (6.1% WER on LibriSpeech test-clean).",
    ),
]


def build_dataset() -> None:
    """Regenerate DATASET_PATH from `samples` (one Sample per abstract)."""
    DATASET_PATH.unlink(missing_ok=True)
    for abstract, target in samples:
        chat = ctl.ChatBedrockAnthropic()
        chat.chat_structured(abstract, data_model=PaperResults)
        chat.export_eval(DATASET_PATH, target=target)


# The scorer grades through Inspect AI's own model registry (separate from
# the chatlas solver below), so it needs an explicit "provider/model-id" --
# same underlying model chatlas defaults to, just addressed Inspect's way.
GRADER_MODEL = "bedrock/us.anthropic.claude-sonnet-4-6"


@task
def papers_eval():
    return Task(
        dataset=json_dataset(str(DATASET_PATH)),
        solver=ctl.ChatBedrockAnthropic().to_solver(data_model=PaperResults),
        scorer=model_graded_fact(model=GRADER_MODEL),
    )


if __name__ == "__main__":
    # `inspect eval` imports this file (sometimes more than once) just to
    # find the @task -- run this directly to (re)build the dataset so that
    # import doesn't trigger live LLM calls as a side effect.
    build_dataset()
    print(f"Wrote {len(samples)} samples to {DATASET_PATH}")
