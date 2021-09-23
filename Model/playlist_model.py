
from pydantic import BaseModel


class PlaylistModel(BaseModel):
    id: str
    title: str
    dance_ability: str
    energy: str
    key: str
    loudness: str
    mode: str
    acoustic_ness: str
    instrumental_ness: str
    live_ness: str
    valence: str
    tempo: str
    duration_ms: str
    time_signature: str
    num_bars: str
    num_sections: str
    num_segments: str
    class_of_song: str

