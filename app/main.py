from fastapi import File, UploadFile

from .models import MFCCResponse
from .settings import app
from .sevice import get_features


@app.post("/py/mfcc/", response_model=MFCCResponse)
async def root(file: UploadFile = File(...)):
    return get_features(file.file)
