from dataclasses import dataclass
from streamlit_product_card import product_card
from streamlit import container, image, subheader, write, columns, button

@dataclass
class Anime:
    id: int
    title: str
    description: str
    image_url: str
    seasons: int
    episodes: int