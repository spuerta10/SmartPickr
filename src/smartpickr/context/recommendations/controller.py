import requests

from shared.base_controller import BaseController
from model.anime import Anime
from context.manager import AppContext, AppContextManager

class RecommendationsController(BaseController):
    __instance = None
    
    def __new__(
            cls, 
            recommender_url: str = None, 
            n_recommendations: int = None, 
            animes: list[Anime] = None
    ):
        if cls.__instance is None:
            cls.__instance: "RecommendationsController" = super().__new__(cls)
            cls.__instance._initialized = False
        return cls.__instance
    
    def __init__(
            self, 
            recommender_url: str = None, 
            n_recommendations: int = None,
            animes: list[Anime] = None
    ):
        if not self._initialized:
            animes = animes or []
            self.recommender_url: str = recommender_url
            self.n_recommendations: int = n_recommendations
            super().__init__(type=AppContext.RECOMMENDATIONS, animes=animes)
            self._initialized = True
        
    def get_recommendations(self) -> list[Anime]:     
        assert self.recommender_url and self.n_recommendations
        try:
            response = requests.post(
                self.recommender_url,
                json={  # TODO: For mantainibility it'd be better to define this in another object
                    "ratings": self.get_user_ratings(), 
                    "n_recommendations": self.n_recommendations
                },
                timeout=600  # 10min
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
    
    def clean_recommendations(self) -> None:
        print('Cleaning recommendations')
        start_recommendations_idx:int = len(self.animes) - self.n_recommendations
        self.animes = self.animes[0:start_recommendations_idx]  # leave calibration animes in the list
        
        