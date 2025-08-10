import streamlit as st

from model.anime import Anime

class Controller:
    def __init__(self, animes: list[Anime]):
        self.animes = animes
        self.__init_session_state()

    def __init_session_state(self) -> None:
        """Initializes the session state for tracking the current anime being rated.
        """
        if "current_anime_index" not in st.session_state:
            st.session_state.current_anime_index = 0    
    
    def get_current_anime(self) -> Anime | None:
        """Retrieves the current anime based on the index stored in session state.

        Returns:
            Anime | None: _description_
        """
        if st.session_state.current_anime_index < len(self.animes):
            return self.animes[st.session_state.current_anime_index]
        return None

    def rate_anime(self, anime_id: int, liked: bool) -> bool:
        """Rates the current anime and stores into DB.

        Args:
            anime_id (int): _description_
            liked (bool): _description_

        Returns:
            bool: _description_
        """
        st.session_state.current_anime_index += 1
        # TODO: Store the rating in a database
        return True
    
    def finished_ratings(self):
        return st.session_state.current_anime_index >= len(self.animes)