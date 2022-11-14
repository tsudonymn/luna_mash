from unittest import TestCase

from assertpy import assert_that

from src.player import Player


class TestPlayer(TestCase):

    def test_init_config(self):
        p = Player()
        assert_that(bot.name).is_equal_to("coco_laptop")
