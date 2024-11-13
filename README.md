# Sketch to Diagram App

Generative AI-powered app to convert pictures and screenshots of hand-drawn sketches into professional diagrams with Mermaid.js.

## Features & flow

1. 📸 Upload images of hand-drawn diagrams or screenshots.
2. 🤖 Generative AI-powered conversion to Mermaid.js format.
3. 🎨 Professional styling and formatting according to brand style guide.
4. 📊 Interact with live preview of generated diagrams.
5. ⬇️ Export Mermaid.js code

## Quick start

### Prerequisites

- Python 3.9+
- Poetry
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sketch-to-diagram.git
cd sketch-to-diagram
```

2. Install dependencies:
```bash
poetry install
```

3. Set up your environment:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### Usage

1. Start the app:
```bash
poetry run streamlit run app/app.py
```

2. Open your browser to the displayed URL (default http://localhost:8501)

3. Upload an image and click "Generate Mermaid Diagram"

## Development

Format code:
```bash
poetry run black app/
```

Run linter:
```bash
poetry run flake8 app/
```

Run tests:
```bash
poetry run pytest
```
