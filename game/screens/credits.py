import pygame
import sys
from pygame.locals import *
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from utils import fade, draw_text


def credits_screen(win, font, mainClock):
    """
    Display the credits screen.

    Args:
        win (pygame.Surface): The game window surface.
        font (pygame.font.Font): The font used for drawing text.
        mainClock (pygame.time.Clock): The game clock.

    Returns:
        None
    """
    running = True

    while running:
        win.fill((0, 0, 0))

        draw_text('Credits', font, (255, 255, 255),
                  win, SCREEN_WIDTH / 2 - 40, 50)
        draw_text('Created by Mihails Danilovs', font, (255, 255,
                  255), win, SCREEN_WIDTH / 2 - 190, SCREEN_HEIGHT / 2 - 100)
        draw_text('md22039', font, (255, 255, 255), win,
                  SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 30)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                fade(win)
                pygame.quit()

                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fade(win)
                    running = False

        pygame.display.update()
        mainClock.tick(24)
