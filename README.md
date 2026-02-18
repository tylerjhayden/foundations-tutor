# foundations-tutor

AI-powered tutor for foundational LLM papers with progressive math scaffolding.

## Quickstart

```bash
pip install foundations-tutor
export ANTHROPIC_API_KEY=sk-ant-...
foundations-tutor
```

## Development

```bash
git clone https://github.com/tylerjhayden/foundations-tutor
cd foundations-tutor
uv sync --dev
uv run foundations-tutor
```

## Overview

`foundations-tutor` is an interactive Streamlit app that teaches the foundational papers
behind modern LLMs (Attention Is All You Need, GPT-2, BERT, etc.) using a Socratic
tutoring approach with spaced repetition and progressive math scaffolding.

- **Catalog**: Browse papers by part/section
- **Lesson**: Interactive tutoring sessions powered by Claude
- **Progress**: Track mastery across concepts
- **Settings**: Configure model, math level, and API key
