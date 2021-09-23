
import uvicorn
from fastapi import FastAPI

from Controller.input_processing_controller import input_processing_router
from Controller.playlists_controller import playlist_router


app = FastAPI()
app.include_router(input_processing_router, prefix='/input', tags=["input"])
app.include_router(playlist_router, prefix='/playlists', tags=["playlists"])

uvicorn.run(app)
