import sys
import os
from fastapi.testclient import TestClient


# Add the project root to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

client = TestClient(app)

def test_summarize_jd():
    response = client.post("/summarize_jd/", files={"file": ("job_description.csv", open("database/job_description.csv", "rb"))})
    assert response.status_code == 200
    assert "summaries" in response.json()

