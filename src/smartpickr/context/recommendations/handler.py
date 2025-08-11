from dataclasses import asdict

import streamlit as st

from model.anime import Anime
from context.recommendations.controller import RecommendationsController 
from shared.views.anime import AnimeView

RECOMMENDATIONS: list[Anime] = [
    Anime(
        id=4,
        title="Fullmetal Alchemist: Brotherhood",
        description="A saiyan’s journey.",
        image_url="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=70,width=320,height=180/catalog/crunchyroll/025260e7ab620e093bff1233dd78629d.jpg",
        seasons=1,
        episodes=64
    ),
    Anime(
        id=5,
        title="Neon Genesis Evangelion",
        description="A saiyan’s journey.",
        image_url="https://wiki.evageeks.org/images/thumb/c/ca/26_C343_shinji-grin.jpg/260px-26_C343_shinji-grin.jpg",
        seasons=1,
        episodes=26
    ),
]

def handle_recommendations() -> None:
    """Display and process anime recommendations.

    This function manages the anime recommendation flow. It retrieves the
    current anime from the `RecommendationsController`, renders it via the
    `AnimeView`, and records the user's rating. If the rating process is not
    finished, it moves to the next recommendation. Once all ratings are done,
    it logs a completion message.

    Steps:
        1. Initialize the recommendations controller with a predefined list of animes.
        2. If there are still animes to rate, get the current one and render it.
        3. Capture the user's "liked" response and update the controller.
        4. Trigger a rerun in Streamlit to show the next anime if applicable.
        5. Print a message when all ratings are completed.

    Returns:
        None
    """
    recommendations_controller = RecommendationsController(animes=RECOMMENDATIONS)
    if not recommendations_controller.finished_ratings():
        current_anime = recommendations_controller.get_current_anime()
        result = AnimeView.render(**asdict(current_anime))
        if result["liked"] is not None: 
            if recommendations_controller.rate_anime(**result):
                st.rerun()  # next recommendation anime
        else:
            print("Finished all ratings!")