
import json

from DataAccess.uow_manager import UOWManager


class InputProcessingProvider:
    def __init__(self):
        pass

    def process(self, file_name):        
        tuple_of_playlists = self.__load_json_data(file_name)

        self.__store_normalized_data(tuple_of_playlists)

    def __load_json_data(self, file_name):
        dict_of_playlist = {}
        tuple_of_playlists = []
        
        with open(f'./Data/{file_name}') as data_file:
            playlist_json = json.load(data_file)
            playlist_json['class_of_song'] = playlist_json.pop('class')

        for attribute_name, attribute_data in playlist_json.items():
            for id_of_song, attribute_value in attribute_data.items():
                if id_of_song not in dict_of_playlist:
                    dict_of_playlist[id_of_song] = dict()

                dict_of_playlist[id_of_song][attribute_name] = attribute_value

        for identity, playlist_data in dict_of_playlist.items():
            tuple_of_playlists.append(tuple(playlist_data.values()))
            
        return tuple_of_playlists

    def __store_normalized_data(self, playlist_models):
        with UOWManager() as uow:
            input_data_access = uow.get_input_process_data_access()

            input_data_access.create_table()
            input_data_access.insert(playlist_models)
