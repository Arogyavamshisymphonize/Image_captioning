import sys
from PIL import Image

from image_captioning.pipeline.captioning_pipeline import initiate_captioning_pipeline
from image_captioning.components.captioning import CaptioningComponent  # your model wrapper
from image_captioning.utils.models import CaptioningModel
from image_captioning.logger import logging
from image_captioning.exceptions import CustomException


class CaptioningInference:
    def __init__(self):
        try:
            logging.info("Initializing CaptioningInference...")
            model = CaptioningModel()
            self.component = CaptioningComponent(model)  # load model here
        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, image_input):
        """
        image_input: can be
            - file path (str)
            - PIL Image
        """
        try:
            if isinstance(image_input, str):
                pil_image = Image.open(image_input).convert("RGB")
            elif isinstance(image_input, Image.Image):
                pil_image = image_input
            else:
                raise ValueError("Unsupported input type")

            caption = initiate_captioning_pipeline(
                component=self.component,
                pil_image=pil_image
            )

            return caption

        except Exception as e:
            logging.error(f"Inference failed: {e}")
            raise CustomException(e, sys)


def main():
    if len(sys.argv) < 2:
        print("Usage: image-captioning-infer <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    inference_obj = CaptioningInference()
    result = inference_obj.predict(image_path)
    print(f"Caption: {result}")

def inference(image_path):
    inference_obj = CaptioningInference()
    result = inference_obj.predict(image_path)
    return result
