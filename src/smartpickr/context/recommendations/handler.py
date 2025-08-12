from dataclasses import asdict

import streamlit as st

from context.recommendations.controller import RecommendationsController 
from context.recommendations.views.loading import LoadingView
from context.manager import AppContextManager, AppContext
from shared.views.anime import AnimeView

def handle_load() -> None:
    controller = RecommendationsController()
    LoadingView.render(controller=controller)
    AppContextManager.on_context_complete(AppContext.LOADING)


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
    controller = RecommendationsController()
    if not controller.finished_ratings():
        current_anime = controller.get_current_anime()
        result = AnimeView.render(**asdict(current_anime))
        if result["liked"] is not None: 
            if controller.rate_anime(**result):
                recommendations: list = controller.get_recommendations(2)
                controller.add_recommendations(recommendations)
                st.rerun()  # next recommendation anime
        else:
            print("Finished all ratings!")