

class InputProcessingDataAccess:
    def __init__(self, cursor):
        self.__cursor = cursor

    def create_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS playlists (
                id TEXT  NOT NULL,
                title TEXT  PRIMARY KEY,
                dance_ability TEXT  NOT NULL,
                energy TEXT NOT NULL,
                key TEXT NOT NULL,
                loudness TEXT NOT NULL,
                mode TEXT NOT NULL,            
                acoustic_ness TEXT  NOT NULL,
                instrumental_ness TEXT NOT NULL,
                live_ness TEXT NOT NULL,
                valence TEXT NOT NULL,
                tempo TEXT NOT NULL,            
                duration_ms TEXT  NOT NULL,
                time_signature TEXT NOT NULL,
                num_bars TEXT NOT NULL,
                num_sections TEXT NOT NULL,
                num_segments TEXT NOT NULL,
                class_of_song TEXT NOT NULL
                ) WITHOUT ROWID;
        """

        self.__cursor.execute(create_table_query)

    def insert(self, tuple_of_playlists):
        bulk_insert_query = """        
            INSERT INTO playlists (id, title, dance_ability, energy, key, loudness, mode, 
            acoustic_ness, instrumental_ness, live_ness, valence, tempo, duration_ms, 
            time_signature, num_bars, num_sections, num_segments, class_of_song)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.__cursor.executemany(bulk_insert_query, tuple_of_playlists)
