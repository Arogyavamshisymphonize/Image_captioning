from image_captioning.constants import MAX_FILE_SIZE, ALLOWED_MIME_TYPES
from fastapi import HTTPException
import magic  # For MIME type detection

def validate_image(contents: bytes):
    """In-memory validation of size and MIME type."""
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File size exceeds 5MB limit.")
    
    mime = magic.from_buffer(contents, mime=True)
    if mime not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {mime}")