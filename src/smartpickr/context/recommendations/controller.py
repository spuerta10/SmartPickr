import requests

from shared.base_controller import BaseController
from model.anime import Anime
from context.manager import AppContext, AppContextManager

class RecommendationsController(BaseController):
    __instance = None
    
    def __new__(cls, recommender_url: str = None, animes: list[Anime] = None):
        if cls.__instance is None:
            cls.__instance: "RecommendationsController" = super().__new__(cls)
            cls.__instance._initialized = False
        return cls.__instance
    
    def __init__(self, recommender_url: str = None, animes: list[Anime] = None):
        if not self._initialized:
            animes = animes or []
            self.recommender_url: str = recommender_url
            super().__init__(type=AppContext.RECOMMENDATIONS, animes=animes)
            self._initialized = True
        
    def get_recommendations(self, n_recommendations: int = 1) -> list[Anime]:     
        assert self.recommender_url
        try:
            response = requests.post(
                self.recommender_url,
                json={  # TODO: For mantainibility it'd be better to define this in another object
                    "ratings": self.get_user_ratings(), 
                    "n_recommendations": n_recommendations
                },
                timeout=600
            )
            response.raise_for_status()
            data: dict = response.json()
            recommendations: list[Anime] = [Anime(**recommendation) for recommendation in data.get("recommendations")]
            return recommendations
        except Exception as e:
            raise e
        
    def add_recommendations(self, recommendations: list[Anime]) -> None:
        self.animes.extend(recommendations)

    def get_recommendations_count(self, liked: bool = True) -> int:
        return sum(1 for rating in self.get_user_ratings() if rating["liked"] == liked)
        
        