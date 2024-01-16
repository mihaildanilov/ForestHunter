import sys
import pygame
from screens.victory import show_victory_screen
from utils.utility_functions import draw_text, fade, fadeStart
from utils.button import Button
from game.game_loop import game_loop
from screens.credits import credits_screen
from settings import SCREEN_WIDTH
from init_game import win, mainClock, main_font, comicsans, mainMenuBg

def main_menu():
    """
    Function to display the main menu of the game.

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
    enemyPick = 6
    score = 0
    bulletsCountLeft = 5
    allBullets = 695

    fadeStart(win, mainMenuBg, main_font)
    
    # Create buttons
    play_button = Button(319, 155, 290, 65, 'Play!', main_font, (0, 0, 0), (31, 35, 50))
    credits_button = Button(319, 255, 290, 65, 'Credits', main_font, (0, 0, 0), (31, 35, 50))
    exit_button = Button(319, 355, 290, 65, 'Exit', main_font, (0, 0, 0), (31, 35, 50))

    victory = False
    main_menuRunning = True
    while main_menuRunning:
        if not victory:
            win.blit(mainMenuBg, (0, 0))
            draw_text('main menu', main_font, (255, 255, 255),
                    win, SCREEN_WIDTH / 2 - 137, 72)
            play_button.draw(win)
            credits_button.draw(win)
            exit_button.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fade(win)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.is_clicked():
                    fade(win)
                    enemyPick, score, bulletsCountLeft, allBullets = game_loop(
                        enemyPick, score, bulletsCountLeft, allBullets)
                elif credits_button.is_clicked():
                    fade(win)
                    credits_screen(win, comicsans, mainClock)
                    fadeStart(win, mainMenuBg, main_font)
                elif exit_button.is_clicked():
                    fade(win)
                    main_menuRunning = False
                    pygame.quit()
                    sys.exit()
        
        if enemyPick > 6:
            result = show_victory_screen(win, comicsans, comicsans)
            if result == "quit":
                fade(win)
                pygame.quit()
                sys.exit()
            elif result == "restart":
                    enemyPick, score, bulletsCountLeft, allBullets = 1, 0, 5, 695  # Reset the game
                    victory = False

        pygame.display.update()
        mainClock.tick(24)
