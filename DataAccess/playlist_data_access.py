
from pydantic import parse_obj_as
from typing import List

from Model.playlist_model import PlaylistModel


class PlaylistsDataAccess:
    def __init__(self, cursor):
        self.__cursor = cursor

    def select(self):
        select_query = """
            SELECT * FROM playlists
        """
        self.__cursor.execute(select_query)
        rows = self.__cursor.fetchall()
        return parse_obj_as(List[PlaylistModel], rows)
