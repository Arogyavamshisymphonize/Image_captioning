CAPTIONING_MODEL = "Salesforce/blip-image-captioning-large"
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_MIME_TYPES = ["image/jpeg", "image/png", "image/webp"]
MAX_GPU_CONCURRENCY = 2  # Adjust based on your VRAM (e.g., 1-3 for 8GB VRAM)