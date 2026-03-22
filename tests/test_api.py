import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from api.main import app

client = TestClient(app)

SAMPLE_SEQUENCE = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCT"


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# ---------------------------------------------------------------------------
# /cluster endpoint
# ---------------------------------------------------------------------------

def test_cluster_returns_cluster_id():
    with patch("api.main.process_sequence", return_value=3):
        response = client.post("/cluster", json={"sequence": SAMPLE_SEQUENCE})
    assert response.status_code == 200
    assert "cluster" in response.json()
    assert response.json()["cluster"] == 3


def test_cluster_returns_500_on_error():
    with patch("api.main.process_sequence", side_effect=RuntimeError("models not found")):
        response = client.post("/cluster", json={"sequence": SAMPLE_SEQUENCE})
    assert response.status_code == 500
    assert "models not found" in response.json()["detail"]


def test_cluster_rejects_missing_sequence():
    response = client.post("/cluster", json={})
    assert response.status_code == 422


# ---------------------------------------------------------------------------
# /classify endpoint
# ---------------------------------------------------------------------------

def test_classify_returns_lineage():
    with patch("api.main.classify_sequence", return_value="BA.2"):
        response = client.post("/classify", json={"sequence": SAMPLE_SEQUENCE})
    assert response.status_code == 200
    assert "lineage" in response.json()
    assert response.json()["lineage"] == "BA.2"


def test_classify_returns_500_when_not_implemented():
    # classify_sequence raises NotImplementedError until a supervised model is trained
    response = client.post("/classify", json={"sequence": SAMPLE_SEQUENCE})
    assert response.status_code == 500
    assert "supervised model" in response.json()["detail"]


def test_classify_rejects_missing_sequence():
    response = client.post("/classify", json={})
    assert response.status_code == 422


# ---------------------------------------------------------------------------
# /utils unit tests
# ---------------------------------------------------------------------------

def test_generate_kmers_length():
    from api.utils import generate_kmers
    sequence = "ATTAAAGGTT"
    kmers = generate_kmers(sequence, k=6)
    assert len(kmers) == len(sequence) - 6 + 1


def test_generate_kmers_content():
    from api.utils import generate_kmers
    kmers = generate_kmers("ATTAAA", k=6)
    assert kmers == ["ATTAAA"]


def test_generate_kmers_short_sequence():
    from api.utils import generate_kmers
    kmers = generate_kmers("ATT", k=6)
    assert kmers == []
