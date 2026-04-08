import os
import sys
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Assuming these imports exist in your project
from image_captioning.logger import logging
from image_captioning.exceptions import CustomException
from image_captioning.entity import Entity, CaptioningEntity

# --- MODEL COMPONENT ---
class CaptioningModel:
    def __init__(self):
        try:
            self.captioning_entity = CaptioningEntity(entity=Entity())
            model_id = self.captioning_entity.captioning_model
            
            self.processor = BlipProcessor.from_pretrained(model_id)
            # Load in FP16 for speed and lower VRAM usage
            self.model = BlipForConditionalGeneration.from_pretrained(
                model_id, 
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
            )
            
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self.model.to(self.device)
            
            # Optional: JIT Compile for Linux/Windows (Torch 2.0+)
            if self.device == "cuda":
                self.model = torch.compile(self.model)
                
            logging.info(f"Model loaded successfully on {self.device}")
        except Exception as e:
            raise CustomException(e, sys)