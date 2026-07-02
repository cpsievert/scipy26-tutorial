# Safe & Maintainable AI Apps in Python

SciPy 2026 tutorial · 4 hours · Carson Sievert (Posit)

## Pre-configured workspace

A computing environment with all of the dependencies needed to run exercises has been made available [here](https://workshop.posit.team).

TODO: shortlink / QR code for workshop environment

## Install

If you want to locally run the tutorial exercises, follow the following instructions to get set up. 

1. Clone the repo

```bash
git clone https://github.com/cpsievert/scipy26-tutorial.git
cd scipy26-tutorial
```

2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) globally

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

If you can't use uv for some reason, Just do what you'd normally do to install the `requirements.txt`

3. Setup a virtual environment

```bash
uv venv
source .venv/bin/activate
```

4. Install dependencies

```bash
uv pip install -r requirements.txt
```

## LLM access

Exercises depend on access to an LLM. Here are a few different ways to get access:

1. Sign up for a free trial at <https://posit.ai/>. No credit card required. You can use the free trial for the entire workshop.

2. Bring your own API key. If you have your own API key, like `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc. that will work just fine.

3. Run a local model on your laptop via **LM Studio** or **Ollama**. No key required, fully private, but slower and requires a beefy laptop. See the [LM Studio docs](https://lmstudio.io/docs/) for setup instructions.

For more choices and details, see https://posit-dev.github.io/chatlas/get-started/models.html


## Exercises

Can be found in the `exercises/` directory

## Solutions

Can be found in the `solutions/` directory

## Resources

Learn more about the tutorial topics at these locations. 

https://posit-dev.github.io/chatlas/
https://posit-dev.github.io/shinychat/py/
https://shiny.posit.co/py/docs/genai-chatbots.html
https://posit-dev.github.io/querychat/py/index.html