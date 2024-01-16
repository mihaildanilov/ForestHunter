import pygame

class Button:
    def __init__(self, x, y, width, height, text, font, color, hover_color):
        """
        Initialize a Button object.

        Args:
        - x (int): The x-coordinate of the button's top-left corner.
        - y (int): The y-coordinate of the button's top-left corner.
        - width (int): The width of the button.
        - height (int): The height of the button.
        - text (str): The text to be displayed on the button.
        - font (pygame.font.Font): The font used for the button's text.
        - color (tuple): The color of the button.
        - hover_color (tuple): The color of the button when the mouse hovers over it.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, win):
        """
        Draw the button on the given surface.

        Args:
        - win (pygame.Surface): The surface on which the button will be drawn.
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(win, self.hover_color, self.rect)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        win.blit(text_surface, (self.x + (self.width - text_surface.get_width()) // 2 ,
                                self.y + (self.height - text_surface.get_height()) // 2 + 5))

    def is_clicked(self):
        """
        Check if the button is clicked.

        Returns:
        - bool: True if the button is clicked, False otherwise.
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return True
        return False
