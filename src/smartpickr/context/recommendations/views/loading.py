from time import sleep

import streamlit as st

from shared.views.base import BaseView
from context.recommendations.controller import RecommendationsController

class LoadingView(BaseView):
    # @override
    @staticmethod
    def render(controller: RecommendationsController) -> dict[None, None]:
        loading_placeholder  = st.empty()
        result_placeholder = st.empty()
        with loading_placeholder.container():
            st.info("🎯 Finding the best anime for you… please wait a moment.")
        with st.spinner("Crunching the otaku magic..."):
            controller.add_recommendations(  # add gotten recommendations
                controller.get_recommendations()
            ) 
        loading_placeholder.empty()
        with result_placeholder.container():
            st.success("✅ Recommendations ready!")
            st.balloons()
            sleep(2)
        result_placeholder.empty()
        
        return {}