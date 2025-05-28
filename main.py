from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import process_sequence, classify_sequence

app = FastAPI()

class SequenceRequest(BaseModel):
    sequence: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/cluster")
def get_cluster(data: SequenceRequest):
    try:
        cluster = process_sequence(data.sequence)
        return {"cluster": cluster}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/classify")
def get_lineage(data: SequenceRequest):
    try:
        label = classify_sequence(data.sequence)
        return {"lineage": label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
