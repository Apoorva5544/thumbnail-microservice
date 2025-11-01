from fastapi import FastAPI, HTTPException
from pydantic import HttpUrl, BaseModel
import requests, io, base64
from PIL import Image

app = FastAPI(title="Thumb-svc")

class UrlIn(BaseModel):
    url: HttpUrl

@app.post("/thumb")
def make_thumb(body: UrlIn, size: int = 150):
    try:
        resp = requests.get(str(body.url), timeout=5)
        resp.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=400, detail="fetch error")
    img = Image.open(io.BytesIO(resp.content))
    img.thumbnail((size, size))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return {"thumb": base64.b64encode(buf.getvalue()).decode()}