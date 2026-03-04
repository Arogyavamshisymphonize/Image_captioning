from src.exceptions import CustomException
from src.logger import logging
import sys
from PIL import Image

def initiate_captioning_pipeline(component, pil_image: Image.Image) -> str:
    try:
        # Use the component passed from the AppState
        caption = component.generate_caption(pil_image)
        return caption
    except Exception as e:
        logging.error(f"Error in captioning pipeline: {e}")
        raise CustomException(e, sys)