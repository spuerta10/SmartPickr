import streamlit as st

from shared.views.base import BaseView
from context.recommendations.controller import RecommendationsController

class SumaryView(BaseView):
    # @override
    @staticmethod
    def render(controller: RecommendationsController):
        st.title("📊 Recommendations Summary")
        
        total_rated: int = len(controller.get_user_ratings())
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="👍 Liked", 
                value=controller.get_recommendations_count(liked=True),
                delta=f"{(controller.get_recommendations_count(liked=True)/total_rated)*100:.1f}%" if total_rated > 0 else "0%"
            )
        with col2:
            st.metric(
                label="👎 Disliked", 
                value=controller.get_recommendations_count(liked=False),
                delta=f"{(controller.get_recommendations_count(liked=False)/total_rated)*100:.1f}%" if total_rated > 0 else "0%"
            )
        with col3:
            st.metric(
                label="📝 Total Rated", 
                value=total_rated
            )
        if controller.get_recommendations_count(liked=True) > controller.get_recommendations_count(liked=False):
            st.info("🌟 You seem to enjoy most of our recommendations! We're getting better at understanding your taste.")
        elif controller.get_recommendations_count(liked=False) > controller.get_recommendations_count(liked=True):
            st.info("🎯 We're learning your preferences. This feedback helps us improve future recommendations!")
        else:
            st.info("⚖️ Your ratings are balanced. This gives us great insight into your preferences!")
        return {}