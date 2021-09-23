
from DataAccess.uow_manager import UOWManager


class PlaylistsProvider:
    def __init__(self):
        pass

    def read_playlists(self):
        with UOWManager() as uow:
            playlists_data_access = uow.get_playlists_data_access()
            return playlists_data_access.select()
