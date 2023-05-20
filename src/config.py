import pygame
import os

from sound import Sound
from theme import Theme


class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(
            os.path.join('../assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('../assets/sounds/capture.wav'))
        self.win_sound = Sound(
            os.path.join('../assets/sounds/win_game.mp3'))
        self.end_sound = Sound(
            os.path.join('../assets/sounds/end_game.mp3'))
        self.lose_sound = Sound(os.path.join('../assets/sounds/lose_game.mp3'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        green = Theme((234, 235, 200), (119, 154, 88))
        brown = Theme((235, 209, 166), (165, 117, 80))
        blue = Theme((229, 228, 200), (60, 95, 135))
        gray = Theme((120, 119, 118), (86, 85, 84))

        self.themes = [green, brown, blue, gray]
