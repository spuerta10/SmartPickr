from dataclasses import asdict

import streamlit as st

from model.anime import Anime
from controller import Controller
from view.anime import AnimeView


ANIMES: list[Anime] = [
    Anime(
        id=1,
        title="Naruto",
        description="A ninja’s journey.",
        image_url="https://imagedelivery.net/LBWXYQ-XnKSYxbZ-NuYGqQ/855e9deb-c452-4d72-4676-f2467ac3ce00/avatarhd",
        seasons=5,
        episodes=220
    ),
    Anime(
        id=2,
        title="One Piece",
        description="A pirate’s journey.",
        image_url="https://static1.cbrimages.com/wordpress/wp-content/uploads/2021/05/One-Piece-Luffy-Funny-Face-1.png?q=50&fit=crop&w=1100&h=618&dpr=1.5",
        seasons=20,
        episodes=1138
    ),
    Anime(
        id=3,
        title="Dragon Ball Z",
        description="A saiyan’s journey.",
        image_url="https://i.pinimg.com/564x/2c/ef/17/2cef171ab11b2a7ed2aba6fedf0d9a0a.jpg",
        seasons=9,
        episodes=291
    )
]

if __name__ == "__main__":
    controller = Controller(animes=ANIMES)
    if not controller.finished_ratings():
        current_anime = controller.get_current_anime()
        result = AnimeView.render(**asdict(current_anime))
        if result["liked"] is not None and controller.rate_anime(**result):
            st.rerun()
