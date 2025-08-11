from dataclasses import dataclass

@dataclass
class Anime:
    id: int
    title: str
    description: str
    image_url: str
    seasons: int
    episodes: int