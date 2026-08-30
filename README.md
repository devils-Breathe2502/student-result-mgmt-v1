# Student Result Management System

A simple Flask + SQLite web app to enter student marks and view computed results.
Built collaboratively via Git branches (frontend, backend, database) and integrated
into `main`, with automated testing via pytest and Continuous Integration via
GitHub Actions.

## Run locally

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000

## Run tests

```bash
pytest -v
```
