#import streamlit as st

from shared.base_controller import BaseController
from context.manager import AppContext
from model.anime import Anime

class RatingController(BaseController):
    def __init__(self, animes: list[Anime]):
        super().__init__(type=AppContext.INITIAL_RATING, animes=animes)