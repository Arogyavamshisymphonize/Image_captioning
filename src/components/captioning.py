import os
import sys
from PIL import Image
import torch

from src.logger import logging
from src.exceptions import CustomException
from src.utils.models import CaptioningModel


class CaptioningComponent:
    def __init__(self, model_obj: CaptioningModel):
        self.model_wrapper = model_obj

    def generate_caption(self, pil_image: Image.Image, text: str = "a photography of") -> str:
        """Synchronous inference logic."""
        try:
            device = self.model_wrapper.device
            # Ensure image is RGB
            if pil_image.mode != "RGB":
                pil_image = pil_image.convert("RGB")

            inputs = self.model_wrapper.processor(
                pil_image, text, return_tensors="pt"
            ).to(device, dtype=torch.float16 if device == "cuda" else torch.float32)
            
            with torch.no_grad():
                out = self.model_wrapper.model.generate(
                    **inputs,
                    max_new_tokens=25,
                    num_beams=1, # Greedy search for lowest latency
                    early_stopping=True
                )
            
            return self.model_wrapper.processor.decode(out[0], skip_special_tokens=True)
        except Exception as e:
            logging.error(f"Inference Error: {e}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        captioning_component = CaptioningComponent()
        img_path = "/home/prem/vamshi/Image_captioning/1347185.png"
        caption = captioning_component.generate_caption(img_path)
        print(f"Generated Caption: {caption}")
    except Exception as e:
        print(f"Pipeline failed: {e}")