# models/

This directory stores trained model files used by the API for inference.

## Expected Files

| File | Description |
|------|-------------|
| `word2vec_sars_cov2.model` | Word2Vec embedding model trained on SARS-CoV-2 k-mers |
| `word2vec_sars_cov2.model.wv.vectors.npy` | Word2Vec weight vectors (auto-generated alongside the model) |
| `kmeans_sars_cov2.pkl` | Fitted KMeans clustering model (10 clusters) |

## How to Generate

Run the model building notebook end-to-end:

```
notebooks/capstone/02_model_building.ipynb
```

At the end of the notebook, save the trained models into this directory:

```python
# Word2Vec
word2vec_model.save("models/word2vec_sars_cov2.model")

# KMeans
import joblib
joblib.dump(kmeans_model, "models/kmeans_sars_cov2.pkl")
```

## Notes

- Model files are excluded from version control via `.gitignore` (they can be large)
- Without these files, the `/cluster` endpoint will return a 500 error
- The `/classify` endpoint is not yet implemented — see the roadmap in the main README
