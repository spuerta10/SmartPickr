from shared.base_controller import BaseController
from model.anime import Anime
from context.manager import AppContext

class RecommendationsController(BaseController):
    def __init__(self, animes: list[Anime]):
        super().__init__(type=AppContext.RECOMMENDATIONS, animes=animes)