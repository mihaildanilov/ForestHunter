# This module contains the main menu screen for the Forest Hunter game.

from pygame.locals import *
import pygame
import sys
from screens.credits import credits_screen
from utils import draw_text, fade, fadeStart, redrawGameWindow
from settings import SCREEN_WIDTH
from init_game import win, mainClock, main_font, comicsans, mainMenuBg
from game.game_loop import game_loop

# Initialize game variables
enemyPick = 1
score = 0
bulletsCountLeft = 5
allBullets = 695

fadeStart(win, mainMenuBg, main_font)
click = False
main_menuRunning = True

# Main menu loop
while main_menuRunning:
    """
    The main menu loop displays the main menu screen and handles user input.

    The loop checks for button clicks and performs the corresponding actions:
    - If the "Play!" button is clicked, it starts the game loop.
    - If the "Credits" button is clicked, it displays the credits screen.
    - If the "Exit" button is clicked, it quits the game.

    The loop also handles events such as quitting the game or pressing the escape key.

    Args:
        None

    Returns:
        None
    """

    win.blit(mainMenuBg, (0, 0))
    draw_text('main menu', main_font, (255, 255, 255),
              win, SCREEN_WIDTH / 2 - 137, 72)
    draw_text('Play!', main_font, (255, 255, 255),
              win, SCREEN_WIDTH / 2 - 56, 165)
    draw_text('Credits', main_font, (255, 255, 255),
              win, SCREEN_WIDTH / 2 - 92, 266)
    draw_text('Exit', main_font, (255, 255, 255),
              win, SCREEN_WIDTH / 2 - 43, 366)

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(314, 150, 300, 75)
    button_2 = pygame.Rect(314, 250, 300, 75)
    button_3 = pygame.Rect(314, 350, 300, 75)

    # Check for button clicks
    if button_1.collidepoint((mx, my)):
        if click:
            fade(win)
            enemyPick, score, bulletsCountLeft, allBullets = game_loop(
                enemyPick, score, bulletsCountLeft, allBullets)

    if button_2.collidepoint((mx, my)):
        if click:
            fade(win)
            credits_screen(win, comicsans, mainClock)
            fadeStart(win, mainMenuBg, main_font)

    if button_3.collidepoint((mx, my)):
        if click:
            fade(win)
            main_menuRunning = False
            pygame.quit()
            sys.exit()

    # Uncomment the following lines to make the button hitboxes visible
    # pygame.draw.rect(win, (255, 0, 0), button_1)
    # pygame.draw.rect(win, (255, 0, 0), button_2)
    # pygame.draw.rect(win, (255, 0, 0), button_3)

    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            fade(win)
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                fade(win)
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pygame.display.update()
    mainClock.tick(24)
