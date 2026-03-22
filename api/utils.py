import os
import numpy as np

# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------
# Trained models are expected at these paths.
# Run notebooks/capstone/02_model_building.ipynb to generate them.

WORD2VEC_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "word2vec_sars_cov2.model")
KMEANS_PATH   = os.path.join(os.path.dirname(__file__), "..", "models", "kmeans_sars_cov2.pkl")

_word2vec_model = None
_kmeans_model   = None

def _load_models():
    global _word2vec_model, _kmeans_model

    if _word2vec_model is None:
        try:
            from gensim.models import Word2Vec
            _word2vec_model = Word2Vec.load(WORD2VEC_PATH)
        except Exception:
            _word2vec_model = None

    if _kmeans_model is None:
        try:
            import joblib
            _kmeans_model = joblib.load(KMEANS_PATH)
        except Exception:
            _kmeans_model = None

# ---------------------------------------------------------------------------
# Core pipeline
# ---------------------------------------------------------------------------

def generate_kmers(sequence, k=6):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

def get_sequence_embedding(sequence, model, k=6):
    """Mean-pool Word2Vec embeddings over all k-mers in the sequence."""
    kmers = generate_kmers(sequence, k)
    vectors = [model.wv[kmer] for kmer in kmers if kmer in model.wv]
    if vectors:
        return np.mean(vectors, axis=0)
    return np.zeros(model.vector_size)

# ---------------------------------------------------------------------------
# API-facing functions
# ---------------------------------------------------------------------------

def process_sequence(sequence):
    """
    Cluster a genome sequence using Word2Vec embeddings + KMeans.
    Returns an integer cluster ID (0-9).

    Requires: models/word2vec_sars_cov2.model, models/kmeans_sars_cov2.pkl
    """
    _load_models()
    if _word2vec_model is None or _kmeans_model is None:
        raise RuntimeError(
            "Trained models not found. Run notebooks/capstone/02_model_building.ipynb "
            "and save outputs to the models/ directory."
        )
    embedding = get_sequence_embedding(sequence, _word2vec_model)
    cluster_id = int(_kmeans_model.predict([embedding])[0])
    return cluster_id

def classify_sequence(sequence):
    """
    Classify a genome sequence into a variant lineage.

    Note: supervised classification was not implemented in the capstone notebooks.
    The clustering pipeline (process_sequence) is the primary inference method.
    This function is a stub pending a trained classification model.
    """
    raise NotImplementedError(
        "Variant classification requires a supervised model trained on labelled lineage data. "
        "See notebooks/capstone/02_model_building.ipynb for the current pipeline."
    )
