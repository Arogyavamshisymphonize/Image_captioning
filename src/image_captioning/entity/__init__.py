from image_captioning.logger import logging
from image_captioning.exceptions import CustomException
from image_captioning.constants import CAPTIONING_MODEL

class Entity:
    def __init__(self):
        self.captioning_model = CAPTIONING_MODEL
        
class CaptioningEntity:
    def __init__(self, entity: Entity):
        self.captioning_model = entity.captioning_model