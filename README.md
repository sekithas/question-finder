# QuestionFinder

Upload an image of an exam question and the AI agent will find which past paper and year it came from.
Errors maybe made because AI is not 100% accurate.

---

## Project Structure

```
question-finder/
├── app.py
├── agents.py
├── tasks.py
├── tools.py
├── vision.py
├── .env
├── static/
│   ├── styles.css
│   └── js/
|       |__scripts.js
└── templates/
    └── index.html
```

---

## Prerequisites

- Python 3.10 or higher
- An [OpenRouter](https://openrouter.ai) API key
- An [EXA](https://exa.ai) API key

---

## How It Works

1. You upload an image of an exam question via the web interface
2. Tesseract (OCR) extracts the raw text from the image locally on your machine
3. The **Finder Agent** uses EXA to search the web for the matching past paper
4. The result (year, month, subject, unit, certificate, examination board) is returned and displayed on screen

---

## Extra Note
 - You will have to install tesseract via homebrew into your computer. Failure to do so will give you TesseractNotFound error.