
from dataclasses import asdict

import streamlit as st

from model.anime import Anime
from context.rating.controller import RatingController
from shared.views.anime import AnimeView
from context.manager import AppContextManager

INIT_RATING: list[Anime] = [
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

def handle_init_rating() -> None:
    """Display and process the initial anime rating phase.

    This function manages the initial anime rating process before generating
    recommendations. It presents each anime in the predefined list to the
    user, collects their feedback, and stores the rating in the application
    context for later use.

    Steps:
        1. Initialize the rating controller with a predefined list of animes.
        2. If there are still animes to rate, retrieve the current one and render it.
        3. Capture the user's "liked" response and record it in the controller.
        4. Store the rating in the application context manager.
        5. Trigger a Streamlit rerun to display the next anime.
        6. Continue until all initial ratings are completed.

    Returns:
        None
    """
    init_rating_controller: RatingController = RatingController(animes=INIT_RATING)
    if not init_rating_controller.finished_ratings():
            current_anime = init_rating_controller.get_current_anime()
            result = AnimeView.render(**asdict(current_anime))
            if result["liked"] is not None and init_rating_controller.rate_anime(**result):
                AppContextManager.set_context_data(result["anime_id"], result["liked"])
                st.rerun()  # next initial rating anime