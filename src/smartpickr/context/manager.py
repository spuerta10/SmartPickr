from enum import Enum
from typing import ClassVar, Any

import streamlit as st

class AppContext(Enum):
    """Enumeration of application contexts used in the workflow."""
    INITIAL_RATING: str = "initial_rating"
    LOADING: str = "loading"
    RECOMMENDATIONS: str = "recommendations"
    COMPLETE: str = "complete"
    
class AppContextManager:
    """Manages the current application context and its associated data."""
    DEFAULT_WORKFLOW: ClassVar[list[AppContext]] = [
        AppContext.INITIAL_RATING,
        AppContext.LOADING,
        AppContext.RECOMMENDATIONS,
        AppContext.COMPLETE
    ]
    
    @staticmethod
    def __set_context(new_context: AppContext) -> None:
        """Set the current application context and trigger a rerun.

        This updates the `st.session_state` with the new context value and
        forces Streamlit to rerun the app so the UI updates accordingly.

        Args:
            new_context (AppContext): The new context to set.
        """
        st.session_state["app_context"] = new_context.value
        st.rerun()  # apply new context
        
    @classmethod
    def get_current_context(cls):
        """Retrieve the current application context.

        If no context is set in `st.session_state`, initializes it with the
        first context in the default workflow.

        Returns:
            AppContext: The current application context.
        """
        if "app_context" not in st.session_state:
            st.session_state["app_context"] = cls.DEFAULT_WORKFLOW[0].value
        return AppContext(st.session_state["app_context"])
    
    @staticmethod
    def set_context_data(key: str, value: Any):
        """Store arbitrary key-value data in the context session.

        Args:
            key (str): The key under which to store the value.
            value (Any): The value to store.
        """
        if "context_data" not in st.session_state:
            st.session_state["context_data"] = {}
        st.session_state["context_data"][key] = value
        
    @staticmethod
    def get_context_data(key: str, default: Any = None) -> None:
        """Retrieve stored context data by key.

        Args:
            key (str): The key for the stored value.
            default (Any, optional): Value to return if key does not exist.
                Defaults to None.

        Returns:
            Any: The stored value or the default if key is not found.
        """
        if "context_data" not in st.session_state:
            st.session_state["context_data"] = {}
        return st.session_state.context_data.get(key, default)
    
    @classmethod
    def on_context_complete(cls, current_context: AppContext) -> None:
        """Mark the current context as complete and advance to the next.

        This removes the current context from the default workflow list and
        sets the next context in sequence. Triggers a rerun to reflect the
        change in the UI.

        Args:
            current_context (AppContext): The context to mark as complete.
        """
        if current_context in cls.DEFAULT_WORKFLOW:
            current_index: int = cls.DEFAULT_WORKFLOW.index(current_context)
            cls.__set_context(cls.DEFAULT_WORKFLOW[current_index + 1])
        cls.__set_context(cls.DEFAULT_WORKFLOW[0])