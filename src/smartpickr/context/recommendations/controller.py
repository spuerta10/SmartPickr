from time import sleep  # TODO: remove after implementing real recommendation logic

from shared.base_controller import BaseController
from model.anime import Anime
from context.manager import AppContext

class RecommendationsController(BaseController):
    __instance = None
    
    def __new__(cls, animes: list[Anime] = None):
        if cls.__instance is None:
            cls.__instance: "RecommendationsController" = super().__new__(cls)
            cls.__instance._initialized = False
        return cls.__instance
    
    def __init__(self, animes: list[Anime] = None):
        if not self._initialized:
            animes = animes or []
            super().__init__(type=AppContext.RECOMMENDATIONS, animes=animes)
            self._initialized = True
        
    def get_recommendations(self, n_recommendations: int = 1) -> list[Anime]:
        sleep(3)  # simulate a delay for fetching recommendations
        mocked_recommendations: list[Anime] = [
            Anime(
                id=4,
                title="Fullmetal Alchemist: Brotherhood",
                description="A saiyan’s journey.",
                image_url="https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=70,width=320,height=180/catalog/crunchyroll/025260e7ab620e093bff1233dd78629d.jpg",
                seasons=1,
                episodes=64
            ),
            Anime(
                id=5,
                title="Neon Genesis Evangelion",
                description="A saiyan’s journey.",
                image_url="https://wiki.evageeks.org/images/thumb/c/ca/26_C343_shinji-grin.jpg/260px-26_C343_shinji-grin.jpg",
                seasons=1,
                episodes=26
            ),
        ]
        
        return mocked_recommendations 
        
    def add_recommendations(self, recommendations: list[Anime]) -> None:
        self.animes.extend(recommendations)
        
        