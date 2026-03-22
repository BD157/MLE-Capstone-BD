# Genome Clustering & Variant Classification
### End-to-End ML Capstone

This project turns SARS-CoV-2 genome analysis from exploratory notebooks into a deployable, service-oriented ML system. It covers the full pipeline — data cleaning, model building, and exposing inference through a FastAPI backend with a Streamlit frontend — with a focus on engineering discipline alongside the modeling work.

---

## Repository Structure

```
MLE-Capstone-BD/
├── api/                          # FastAPI backend
│   ├── main.py                   # Endpoints: /health, /cluster, /classify
│   └── utils.py                  # Sequence processing and classification logic
├── frontend/
│   └── app.py                    # Streamlit UI
├── notebooks/
│   ├── capstone/                 # Core capstone work
│   │   ├── 01_aws_data_cleaning.ipynb
│   │   ├── 02_model_building.ipynb
│   │   ├── 03_memory_batching.ipynb
│   │   ├── 04_ray_parallel.ipynb
│   │   └── 05_data_cleaning_merging.py
│   └── mini-projects/            # Supporting MLE mini-projects
│       ├── 01_ml_fundamentals.ipynb
│       ├── 02_customer_churn_model.ipynb
│       ├── 03_flask_deployment.ipynb
│       └── 04_recommendation_engines.ipynb
├── datasets/                     # Data acquisition scripts
│   ├── 01_ncbi_dataset.py
│   ├── 02_ena_dataset.py
│   └── 03_cdc_dataset.py
├── research/                     # Embedding experiments
│   ├── 01_word2vec.py
│   ├── 02_kmer2vec.py
│   └── 03_virtifier.py
├── Dockerfile
├── render.yaml
└── requirements.txt
```

---

## Local Setup

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

API available at `http://localhost:8000`

## Docker

```bash
docker build -t genome-api .
docker run -p 8000:10000 genome-api
```

## Streamlit

Update the `API_URL` in `frontend/app.py` with your Render URL, then deploy on Streamlit Cloud.

---

## API Endpoints

Hosted via [Render](https://render.com). Interactive docs at `/docs` (Swagger) and `/redoc`.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/cluster` | Cluster a genome sequence |
| POST | `/classify` | Classify a sequence into a variant lineage |

---

## Scope

**Done**
- Data cleaning and model building notebooks
- FastAPI inference service (cluster + classify endpoints)
- Streamlit UI
- Docker + Render deployment

**Planned**
- Replace placeholder model logic with trained models
- Add unit and integration tests
- Set up CI/CD
- Version models and datasets

---

## Author

Built by BD as part of a machine learning engineering capstone.
