
## Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) ≥ 1.9
- Python ≥ 3.10
- An LLM API key (Anthropic, OpenAI, etc.) **or** [LM Studio](https://lmstudio.ai/) for local models

Install the Python packages needed for the exercises:

```bash
pip install chatlas shinychat querychat "querychat[viz]" requests shiny faicons
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
make serve DECK=02-chatlas
```

Open all rendered decks in the browser at once:

```bash
make preview
```

## Running exercises

Each exercise is a standalone Python file:

```bash
# chatlas (runs in the terminal)
python exercises/01-chatlas-starter.py

# shinychat / querychat (opens in the browser)
shiny run exercises/02-shinychat-starter.py
shiny run exercises/03-querychat-starter.py
```

## Make targets

| Target | Description |
|--------|-------------|
| `make help` | Show all targets |
| `make slides` | Render all slide decks |
| `make serve DECK=<name>` | Live-preview a single deck |
| `make preview` | Open all decks in the browser |
| `make clean` | Remove rendered HTML and supporting files |
