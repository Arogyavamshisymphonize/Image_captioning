from src.logger import logging
from src.exceptions import CustomException
from src.constants import CAPTIONING_MODEL

class Entity:
    def __init__(self):
        self.captioning_model = CAPTIONING_MODEL
        
class CaptioningEntity:
    def __init__(self, entity: Entity):
        self.captioning_model = entity.captioning_model