"""
This module initializes the game by setting up the display, loading assets, and playing background music.

Functions:
    - None

Variables:
    - win: The game window created using pygame.display.set_mode().
    - icon: The game icon loaded from the assets.
    - main_font: The main font used in the game loaded from the assets.
    - comicsans: The Comic Sans font used in the game loaded from the assets.
    - bg: The background image loaded from the assets.
    - mainMenuBg: The main menu background image loaded from the assets.
    - sprites: The sprites loaded from the assets.
    - mainClock: The clock used to control the frame rate of the game.
    - sounds: The sounds loaded from the assets.
    - hitSound: The hit sound loaded from the assets.
    - music: The background music loaded from the assets.
"""

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from assets import assets

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = assets.load_image("sprites/icon/robe5.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Forest Hunter")

main_font = assets.load_fonts()['main_font']
comicsans = assets.load_fonts()['comicsans']

bg = assets.load_image("sprites/bg/gameBg.png")
mainMenuBg = assets.load_image("sprites/bg/mainMenuBg.png")

sprites = assets.load_sprites()

mainClock = pygame.time.Clock()

sounds = assets.load_sounds()
hitSound = sounds['hit_sound']
music = sounds['background_music']
pygame.mixer.music.set_volume(0.01)
hitSound.set_volume(0.01)
pygame.mixer.music.play(loops=-1)
