from streamlit_product_card import product_card
import streamlit as st

from view.base import BaseView

class AnimeView(BaseView):
    # @override
    @staticmethod
    def render(
        id: int, 
        title: str, 
        description: str, 
        image_url: str, 
        seasons: int, 
        episodes: int
    ) -> dict[str, int | bool]:
        liked: None | bool = None

        product_card(
            product_name=title,
            description=description,
            product_image=image_url,
            key=f"{id}",
            picture_position="top",
            image_aspect_ratio="16/9",
            image_object_fit="cover",
        )
        col1, col2 = st.columns(2)
        with col1:
            _, center, _ = st.columns([1, 2, 1])
            with center:
                if st.button("👍 Upvote!"):
                    liked = True
        with col2:
            _, center, _ = st.columns([1, 2, 1])
            with center:
                if st.button("👎 Downvote!"):
                    liked = False

        return {
            "anime_id" : id,
            "liked" :  liked
        }