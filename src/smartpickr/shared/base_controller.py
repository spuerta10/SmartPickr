import streamlit as st

from context.manager import AppContext, AppContextManager
from model.anime import Anime

class BaseController:
    """Base controller for managing anime rating workflows.

    Handles tracking the current anime to rate, storing ratings,
    and progressing through the anime list.
    """
    def __init__(self, type: AppContext, animes: list[Anime]):
        """Initialize the base controller.

        Args:
            type (AppContext): The application context this controller manages.
            animes (list[Anime]): The list of animes to process.
        """
        self.type = type
        self.animes = animes
        self.session_key: str = f"{self.type}_current_anime_index"
        self.__init_session_state()

    def __init_session_state(self) -> None:
        """Initialize session state for the current anime index.

        If the index is not already set in `st.session_state`,
        initializes it to 0.
        """
        if self.session_key not in st.session_state:
            st.session_state[self.session_key] = 0    
        
        if "user_ratings" not in st.session_state:
            st.session_state.user_ratings = []
    
    @staticmethod
    def __store_rating(anime_id: int, liked: bool) -> None:
        """Store the user's rating for a given anime.

        Args:
            anime_id (int): The ID of the anime being rated.
            liked (bool): Whether the user liked the anime.
        """
        st.session_state.user_ratings.append(
            {"anime_id":anime_id,"liked":liked}
        )
        
    def get_current_anime(self) -> Anime | None:
        """Retrieve the current anime based on the session index.

        Returns:
            Anime | None: The current `Anime` instance, or `None` if all animes
            have been rated.
        """
        if st.session_state[self.session_key] < len(self.animes):  # TODO: do a pop would be better 
            return self.animes[st.session_state[self.session_key]]
        return None
    
    def rate_anime(self, anime_id: int, liked: bool) -> bool:
        """Rate the current anime and advance to the next.

        Args:
            anime_id (int): The ID of the anime being rated.
            liked (bool): Whether the user liked the anime.

        Returns:
            bool: True if rating was recorded and moved to next anime.
        """
        st.session_state[self.session_key] += 1
        self.__store_rating(anime_id, liked)
        return True
    
    @staticmethod
    def get_user_ratings() -> dict[int, bool]:
        """Retrieve all stored user ratings.

        Returns:
            dict[int, bool]: A copy of the user's ratings where keys are anime IDs
            and values are booleans indicating like/dislike.
        """
        return st.session_state.user_ratings.copy()
    
    def finished_ratings(self):
        """Check if all animes have been rated and update context if so.

        If the current anime index is equal to or greater than the number of
        animes in the list, triggers the `on_context_complete` method of
        `AppContextManager` to move to the next context.

        Returns:
            bool: True if all ratings are complete, False otherwise.
        """
        if self.session_key not in st.session_state:
            st.session_state[self.session_key] = 0   # TODO: discover why this is necesary

        if st.session_state[self.session_key] >= len(self.animes):
            AppContextManager.on_context_complete(self.type)
            return True
        return False