from unittest import TestCase

from assertpy import assert_that
from pygame import Rect

from src.movement import is_within_horz_bounds
from src.settings import SCREEN_WIDTH


class TestMovement(TestCase):

    def test_in_bounds(self):
        r = Rect(1, 1, 10, 10)

        assert_that(is_within_horz_bounds(r)).is_true()

    def test_out_of_bounds_left(self):
        r = Rect(-1, 1, 10, 10)

        assert_that(is_within_horz_bounds(r)).is_false()

    def test_out_of_bounds_right(self):
        r = Rect(SCREEN_WIDTH + 1, 1, 10, 10)

        assert_that(is_within_horz_bounds(r)).is_false()


