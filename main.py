from fastapi import FastAPI, HTTPException
from models import TextRequest
from services import text_analysis

app = FastAPI()

@app.post("/analyze")
def analyze_text(request: TextRequest):
    text = request.text.lower()

    if not text:
        raise HTTPException(status_code=400, detail="Text Cannot be empty")
    
    analysis_result =  text_analysis(text=text)

    return analysis_result   