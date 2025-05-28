# Genome Clustering & Variant Classification API

Production-ready app for clustering and classifying SARS-CoV-2 genome sequences.

## Local Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker

```bash
docker build -t genome-api .
docker run -p 8000:8000 genome-api
```

## Streamlit

Update streamlit_app/app.py with your Render API URL and deploy on Streamlit Cloud.

## 📡 API (Hosted via Render)

- `/health`
- `/cluster`
- `/classify`
