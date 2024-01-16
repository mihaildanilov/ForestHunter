import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


def redrawGameWindow(
        win,
        font,
        score,
        bulletsCountLeft,
        allBullets,
        man,
        enemy,
        bullets,
        bg):
    """
    Redraws the game window with the updated game elements.

    Args:
        win (pygame.Surface): The game window surface.
        font (pygame.font.Font): The font used for rendering text.
        score (int): The current score.
        bulletsCountLeft (int): The number of bullets left.
        allBullets (int): The total number of bullets.
        man (Player): The player object.
        enemy (Enemy): The enemy object.
        bullets (list): A list of Bullet objects.
        bg (pygame.Surface): The background image.

    Returns:
        None
    """
    win.blit(bg, (0, -150))  # background image pushed by 150 pixels up
    text = font.render('Score: ' + str(score), 1,
                       (45, 84, 145))  # score text
    bulletsLeft = font.render(
        "Bullets left " +
        str(bulletsCountLeft) +
        "  /  " +
        str(allBullets),
        1,
        (45,
         84,
         145))  # bullets left text
    win.blit(text, ((SCREEN_WIDTH - 200), 10))  # score text position
    # bullets left text position
    win.blit(bulletsLeft, ((SCREEN_WIDTH - 550), 10))
    man.draw(win)   # player draw
    enemy.draw(win)  # enemy draw
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    """
    Draws text on the specified surface.

    Args:
        text (str): The text to be displayed.
        font (pygame.font.Font): The font used for rendering the text.
        color (tuple): The color of the text in RGB format.
        surface (pygame.Surface): The surface on which the text will be drawn.
        x (int): The x-coordinate of the top-left corner of the text.
        y (int): The y-coordinate of the top-left corner of the text.

    Returns:
        None
    """
    obj = font.render(text, 1, color)
    rect = obj.get_rect()
    rect.topleft = (x, y)
    surface.blit(obj, rect)


def fade(win):
    """
    Fades the game window to black.

    Args:
        win (pygame.Surface): The game window surface.

    Returns:
        None
    """
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        win.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(7)


def fadeStart(win, mainMenuBg, main_font):
    """
    Fades the game window at the start of the game.

    Args:
        win (pygame.Surface): The game window surface.
        mainMenuBg (pygame.Surface): The background image for the main menu.
        main_font (pygame.font.Font): The font used for rendering text in the main menu.

    Returns:
        None
    """
    fadeStart = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fadeStart.fill((0, 0, 0))
    for alpha in range(255, 0, -5):
        fadeStart.set_alpha(alpha)
        win.blit(mainMenuBg, (0, 0))
        win.blit(fadeStart, (0, 0))
        pygame.display.update()
        pygame.event.pump()
