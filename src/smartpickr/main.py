from context.manager import AppContextManager, AppContext
from context.rating.handler import handle_init_rating
from shared.views.loading import LoadingView
from context.recommendations.handler import handle_recommendations

if __name__ == "__main__":
    if AppContextManager.get_current_context() == AppContext.INITIAL_RATING:
        handle_init_rating()
        
    elif AppContextManager.get_current_context() == AppContext.LOADING:
        LoadingView.render()
        AppContextManager.on_context_complete(AppContext.LOADING)
    
    elif AppContextManager.get_current_context() == AppContext.RECOMMENDATIONS:
        handle_recommendations()
