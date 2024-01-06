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



def draw_text(text, font, color, surface, x, y):
    obj = font.render(text, 1, color)
    rect = obj.get_rect()
    rect.topleft = (x, y)
    surface.blit(obj, rect)

def fade(win):
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        win.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(7)


def fadeStart(win,mainMenuBg,main_font):
    fadeStart = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fadeStart.fill((0, 0, 0))
    for alpha in range(255, 0, -5):
        fadeStart.set_alpha(alpha)
        win.blit(mainMenuBg, (0, 0))
        draw_text('main menu', main_font, (255, 255, 255),
                  win, SCREEN_WIDTH / 2 - 137, 72)
        draw_text('Play!', main_font, (255, 255, 255),
                  win, SCREEN_WIDTH/2 - 56, 165)
        draw_text('Credits', main_font, (255, 255, 255),
                  win, SCREEN_WIDTH/2 - 92, 266)
        draw_text('Exit', main_font, (255, 255, 255),
                  win, SCREEN_WIDTH/2-43, 366)
        win.blit(fadeStart, (0, 0))
        pygame.display.update()
        pygame.event.pump()