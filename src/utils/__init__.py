from src.utils.models import CaptioningModel
from src.utils.app_state import AppState
from src.components.captioning import CaptioningComponent

from src.logger import logging
from src.exceptions import CustomException
import sys


from fastapi import FastAPI

state = AppState()
async def lifespan(app: FastAPI):
    """Handles startup/shutdown logic (Model Loading)."""
    logging.info("Initializing ML Resources...")
    model_instance = CaptioningModel()
    state.component = CaptioningComponent(model_instance)
    yield
    logging.info("Cleaning up ML Resources...")
    del state.component