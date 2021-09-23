
from .input_processing_data_access import InputProcessingDataAccess
from .playlist_data_access import PlaylistsDataAccess


class UOW:
    def __init__(self, cursor):
        self.__cursor = cursor

    def get_input_process_data_access(self):
        return InputProcessingDataAccess(self.__cursor)

    def get_playlists_data_access(self):
        return PlaylistsDataAccess(self.__cursor)
