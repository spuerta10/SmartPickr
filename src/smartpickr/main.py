import streamlit as st

from context.manager import AppContextManager, AppContext
from context.rating.handler import handle_init_rating
#from context.recommendations.views.loading import LoadingView
from context.recommendations.handler import handle_load, handle_recommendations

if __name__ == "__main__":
    if AppContextManager.get_current_context() == AppContext.INITIAL_RATING:
        handle_init_rating()
        
    elif AppContextManager.get_current_context() == AppContext.LOADING:
        handle_load()
    
    elif AppContextManager.get_current_context() == AppContext.RECOMMENDATIONS:
        handle_recommendations()
    
    elif AppContextManager.get_current_context() == AppContext.COMPLETE:
        st.session_state.clear()  # wipe all session variables
        st.rerun()  # restart the script from top
