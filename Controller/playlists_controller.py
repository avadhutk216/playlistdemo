

from sqlite3 import OperationalError
from fastapi import APIRouter
from fastapi import HTTPException


from Providers.playlists_provider import PlaylistsProvider

playlist_router = APIRouter()


@playlist_router.get("/")
async def get_playlists():
    playlists_provider = PlaylistsProvider()
    return playlists_provider.read_playlists()
