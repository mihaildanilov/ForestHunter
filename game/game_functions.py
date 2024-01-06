import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
def redrawGameWindow(win,font,score, bulletsCountLeft, allBullets,man,enemy,bullets,bg):
    win.blit(bg, (0, -150))  # background image pushed by 150 pixels up
    text = font.render('Score: ' + str(score), 1,
                            (45, 84, 145))  # score text
    bulletsLeft = font.render(
        "Bullets left " + str(bulletsCountLeft) + "  /  " + str(allBullets), 1, (45, 84, 145))  # bullets left text
    win.blit(text, ((SCREEN_WIDTH - 200), 10))  # score text position
    # bullets left text position
    win.blit(bulletsLeft, ((SCREEN_WIDTH - 550), 10))
    man.draw(win)   # player draw
    enemy.draw(win)  # enemy draw
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()