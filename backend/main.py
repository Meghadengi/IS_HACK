from fastapi import FastAPI, UploadFile, File
import pandas as pd

from fastapi.staticfiles import StaticFiles
#from main import app
from pypdf import PdfReader


def test_summarize_jd():
    response = client.post("/summarize_jd/", files={"file": ("job_description.csv", open("path/to/job_description.csv", "rb"))})
    assert response.status_code == 200
    assert "summaries" in response.json()

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.post("/summarize_jd/")
async def summarize_jd(file: UploadFile = File(...)):
    jd_df = pd.read_csv(file.file, encoding='latin1')
    print(jd_df.columns)  # Add this line to print column names
    summaries = jd_df['Job Description'].apply(lambda x: x[:100])  # Update with correct column name
    return {"summaries": summaries.tolist()}


@app.post("/parse_cv/")
async def parse_cv(file: UploadFile = File(...)):
    reader = PdfReader(file.file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return {"cv_text": text[:200]}  # Example: first 200 chars
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@app.post("/match_candidates/")
async def match_candidates(jd_summary: str, cv_text: str):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([jd_summary, cv_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return {"match_score": score[0][0]}
import smtplib
from email.mime.text import MIMEText

@app.post("/send_email/")
async def send_email(to_address: str, subject: str, body: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "you@example.com"
    msg['To'] = to_address

    try:
        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)
        return {"status": "Email sent successfully"}
    except Exception as e:
        return {"status": "Failed to send email", "error": str(e)}