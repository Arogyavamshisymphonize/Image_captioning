from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import io
import asyncio
import sys

from src.utils.lifespan import lifespan, state # Import our shared state
from src.logger import logging
from src.exceptions import CustomException
from src.utils.validations import validate_image
from src.pipeline.captioning_pipeline import initiate_captioning_pipeline

app = FastAPI(title="High-Performance Captioning API", lifespan=lifespan)

@app.post("/predict")
async def predict_caption(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        validate_image(contents)
        
        img_buffer = io.BytesIO(contents)
        pil_img = Image.open(img_buffer)
        
        async with state.semaphore:
            # We pass the pre-loaded component from state into the pipeline
            caption = await asyncio.to_thread(
                initiate_captioning_pipeline, 
                state.captioning_component, 
                pil_img
            )

        return {"success": True, "filename": file.filename, "caption": caption}

    except Exception as e:
        logging.error(f"API Route Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Inference failed.")

@app.get("/health")
async def health():
    # Check if the component is actually loaded in state
    is_ready = state.captioning_component is not None
    return {
        "status": "ready" if is_ready else "loading",
        "slots_free": state.semaphore._value
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)