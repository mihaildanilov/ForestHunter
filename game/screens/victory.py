from settings import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from utils.button import Button

def show_victory_screen(win, font, main_font):
    """
    Shows the victory screen with options to quit or restart.

    Args:
        win (pygame.Surface): The game window surface.
        font (pygame.font.Font): The font used for rendering the victory message.
        main_font (pygame.font.Font): The font used for rendering button texts.

    Returns:
        str: "quit" if the quit button is clicked, "restart" if the restart button is clicked.
    """
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0))  # Semi-transparent black overlay
    win.blit(overlay, (0, 0))

    victory_text = font.render('Victory!', True, (255, 215, 0))
    win.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, 150))

    quit_button = Button(SCREEN_WIDTH // 2 - 250, 300, 100, 50, 'Quit', main_font, (170, 0, 0), (255, 0, 0))
    restart_button = Button(SCREEN_WIDTH // 2 + 150, 300, 125, 50, 'Restart', main_font, (0, 170, 0), (0, 255, 0))

    quit_button.draw(win)
    restart_button.draw(win)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        if quit_button.is_clicked():
            return "quit"
        if restart_button.is_clicked():
            return "restart"

    return None
