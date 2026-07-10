
## Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) ≥ 1.9
- Python ≥ 3.10
- An LLM API key (Anthropic, OpenAI, etc.) **or** [LM Studio](https://lmstudio.ai/) for local models

Install the Python packages needed for the exercises:

```bash
pip install -r requirements.txt
```

## Building slides

```bash
make slides    # render all decks
make clean     # remove rendered HTML
```

Individual decks rebuild automatically when their `.qmd` or `theme.scss` changes.

## Developing slides

Live-preview a single deck with hot reload:

```bash
make serve DECK=02-basics
```

Open all rendered decks in the browser at once:

```bash
make preview
```

## Running exercises

Each exercise is a standalone Python file:

```bash
# pure chatlas (runs in the terminal)
python exercises/00-chat-hello.py

# shinychat / querychat (opens in the browser)
shiny run exercises/shinychat-app.py
```

## Make targets

| Target | Description |
|--------|-------------|
| `make help` | Show all targets |
| `make slides` | Render all slide decks |
| `make serve DECK=<name>` | Live-preview a single deck |
| `make preview` | Open all decks in the browser |
| `make clean` | Remove rendered HTML and supporting files |
