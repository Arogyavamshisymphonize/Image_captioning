import asyncio

class AppState:
    def __init__(self):
        self.captioning_component = None  # Will be filled by lifespan
        self.semaphore = asyncio.Semaphore(2) # Limit concurrent GPU tasks