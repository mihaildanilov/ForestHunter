from pygame.locals import *
import pygame
import sys
from screens.credits import credits_screen
from utils import draw_text, fade, fadeStart, redrawGameWindow
from settings import SCREEN_WIDTH
from init_game import win, mainClock, main_font, comicsans, bg, mainMenuBg, sprites, hitSound
from game.game_loop import game_loop

bulletsCountLeft = 5
allBullets = 695

def main_menu():
    enemyPick = 1
    score = 0
    bulletsCountLeft = 5
    allBullets = 695
    fadeStart(win, mainMenuBg, main_font)
    click = False
    main_menuRunning = True
    while main_menuRunning:

        win.blit(mainMenuBg, (0, 0))
        draw_text('main menu', main_font, (255, 255, 255),
                  win, SCREEN_WIDTH / 2 - 137, 72)
        draw_text('Play!', main_font, (255, 255, 255),
                  win, SCREEN_WIDTH/2 - 56, 165)
        draw_text('Credits', main_font, (255, 255, 255),
                  win, SCREEN_WIDTH/2 - 92, 266)
        draw_text('Exit', main_font, (255, 255, 255),
                  win, SCREEN_WIDTH/2-43, 366)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(314, 150, 300, 75)
        button_2 = pygame.Rect(314, 250, 300, 75)
        button_3 = pygame.Rect(314, 350, 300, 75)

        if button_1.collidepoint((mx, my)):
            if click:
                fade(win)
                enemyPick, score, bulletsCountLeft,allBullets=game_loop(enemyPick, score, bulletsCountLeft,allBullets)

        if button_2.collidepoint((mx, my)):
            if click:
                fade(win)
                credits_screen(win,comicsans,mainClock)
                fadeStart(win, mainMenuBg, main_font)

        if button_3.collidepoint((mx, my)):
            if click:
                fade(win)
                main_menuRunning = False
                pygame.quit()
                sys.exit()

        # Main menu button hitbox
        # pygame.draw.rect(win, (255, 0, 0), button_1)    #comment to make invisible
        # pygame.draw.rect(win, (255, 0, 0), button_2)    #comment to make invisible
        # pygame.draw.rect(win, (255, 0, 0), button_3)    #comment to make invisible

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

main_menu()
pygame.quit()
