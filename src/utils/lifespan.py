from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.utils.app_state import AppState
from src.utils.models import CaptioningModel
from src.components.captioning import CaptioningComponent
from src.logger import logging

state = AppState()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Lifespan starting: Loading Model into VRAM...")
    try:
        model_obj = CaptioningModel()
        # Store the loaded component in our state object
        state.captioning_component = CaptioningComponent(model_obj)
        yield
    finally:
        logging.info("Lifespan shutting down: Cleaning up VRAM...")
        del state.captioning_component