# AI_Resume_Enhancer_backend
Backend for AI Resume Enhancer
## Features

- RESTful API built with Flask
- Integrates Langchain for advanced language processing
- Utilizes Fitz for PDF parsing and manipulation

## Requirements

- Python 3.8+
- Flask
- Langchain
- Fitz (PyMuPDF)

## Installation

```bash
git clone https://github.com/yourusername/AI_Resume_Enhancer_backend.git
cd AI_Resume_Enhancer_backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

```bash
export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
flask run
```

The API will be available at `http://127.0.0.1:5000/`.

## Usage

- Send resume PDFs to the API endpoint.
- The backend uses Fitz to extract text, Langchain for enhancement, and returns improved content.

## License

MIT License