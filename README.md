# Genome Clustering & Variant Classification
**End-to-End ML Capstone | SARS-CoV-2 Genomic Surveillance**

> Can machine learning read a virus? This project finds out.

Taking raw SARS-CoV-2 genome sequences and turning them into a live, queryable API — this capstone covers the full ML engineering journey: sourcing genomic data, cleaning it at scale, training embedding models, and shipping inference as a production-ready service with Docker and cloud deployment.

The focus is as much on **how** the system is built as on the models themselves — structured code, clean separation of concerns, and a pipeline that can actually be run by someone other than the person who wrote it.

---

## What It Does

Feed it a genome sequence. Get back a cluster ID or variant lineage.

Under the hood:
- Genome sequences are broken into overlapping **6-mer fragments**
- A **Word2Vec model** learns embeddings for each k-mer based on genomic context
- Sequences are represented as the **mean embedding** of their k-mers
- **KMeans clustering** groups sequences by genomic similarity

The result is a REST API that runs locally, in Docker, or on the cloud — with a Streamlit UI for interactive exploration.

---

## Repository Structure

```
MLE-Capstone-BD/
├── api/                          # FastAPI backend
│   ├── main.py                   # Endpoints: /health, /cluster, /classify
│   └── utils.py                  # k-mer pipeline, embedding, clustering logic
├── frontend/
│   └── app.py                    # Streamlit UI
├── notebooks/
│   ├── capstone/                 # Core capstone work, in order
│   │   ├── 01_aws_data_cleaning.ipynb      # Large-scale data cleaning on AWS
│   │   ├── 02_model_building.ipynb         # Word2Vec + KMeans training & evaluation
│   │   ├── 03_memory_batching.ipynb        # Handling large sequences with batching
│   │   ├── 04_ray_parallel.ipynb           # Parallel processing with Ray
│   │   └── 05_data_cleaning_merging.py     # Merging FASTA + metadata pipelines
│   └── mini-projects/            # Supporting MLE work
│       ├── 01_ml_fundamentals.ipynb
│       ├── 02_customer_churn_model.ipynb
│       ├── 03_flask_deployment.ipynb
│       └── 04_recommendation_engines.ipynb
├── datasets/                     # Data acquisition scripts (NCBI, ENA, CDC)
│   ├── 01_ncbi_dataset.py
│   ├── 02_ena_dataset.py
│   └── 03_cdc_dataset.py
├── research/                     # Embedding approach experiments
│   ├── 01_word2vec.py
│   ├── 02_kmer2vec.py
│   └── 03_virtifier.py
├── models/                       # Trained model files (generated from 02_model_building.ipynb)
├── Dockerfile
├── render.yaml
└── requirements.txt
```

---

## Quickstart

**Run locally**
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```
API at `http://localhost:8000` — interactive docs at `/docs`

**Run with Docker**
```bash
docker build -t genome-api .
docker run -p 8000:10000 genome-api
```

**Streamlit UI**

Update `API_URL` in `frontend/app.py` with your Render URL, then deploy on Streamlit Cloud.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/cluster` | Returns a cluster ID for a given genome sequence |
| POST | `/classify` | Returns the predicted variant lineage |

> To use the clustering endpoint with real predictions, train and save models from `notebooks/capstone/02_model_building.ipynb` into the `models/` directory.

---

## The Data

Genomic sequences sourced from three public datasets:

| Source | Script | Coverage |
|--------|--------|----------|
| [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/) | `datasets/01_ncbi_dataset.py` | Full genome sequences via Entrez API |
| [ENA](https://www.ebi.ac.uk/ena/) | `datasets/02_ena_dataset.py` | Up to 50,000 SARS-CoV-2 genomes |
| [CDC GitHub](https://github.com/cdcepi) | `datasets/03_cdc_dataset.py` | U.S. variant surveillance by state |

---

## Engineering Highlights

- **Notebook → Service pipeline** — research code lives in notebooks; inference logic lives in `api/`. Clean boundary, no leakage.
- **Scalable preprocessing** — memory batching (`03_memory_batching.ipynb`) and Ray parallelism (`04_ray_parallel.ipynb`) for processing sequences that don't fit in memory
- **Three embedding approaches explored** — Word2Vec, K-mer2Vec, and Virtifier compared in `research/`
- **Cloud-ready** — Dockerfile + Render config included, deployable in minutes

---

## Roadmap

- [ ] Save and version trained models into `models/`
- [ ] Wire up real KMeans predictions in the API
- [ ] Build a supervised classifier for variant lineage prediction
- [ ] Add unit and integration tests
- [ ] Set up CI/CD pipeline

---

## Author

Built by BD as part of a machine learning engineering capstone.
