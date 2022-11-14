from pygame import Rect

from src.settings import SCREEN_WIDTH


def is_within_horz_bounds(rect: Rect):
    return 0 <= rect.left and rect.right <= SCREEN_WIDTH
