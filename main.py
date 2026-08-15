from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import hashlib

app = FastAPI(title="URL Shortener API")

# In-memory storage for shortened URLs
url_db = {}

class URLRequest(BaseModel):
    url: HttpUrl

@app.get("/")
def home():
    return {"message": "URL Shortener API is running successfully!"}

@app.post("/shorten")
def shorten_url(request: URLRequest):
    original_url = str(request.url)
    
    # Generate 6-character unique hash
    short_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]
    url_db[short_hash] = original_url
    
    return {
        "short_code": short_hash,
        "original_url": original_url,
        "short_url": f"http://localhost:8000/{short_hash}"
    }

@app.get("/{short_code}")
def redirect_url(short_code: str):
    if short_code not in url_db:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return {"redirect_to": url_db[short_code]}