from fastapi import FastAPI, UploadFile, File
from datetime import datetime
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_log(file: UploadFile = File(...)):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = file.filename.replace("/", "_")
    out_path = os.path.join(UPLOAD_DIR, f"{ts}_{safe_name}")

    data = await file.read()
    with open(out_path, "wb") as f:
        f.write(data)

    return {"saved_as": out_path, "bytes": len(data)}
