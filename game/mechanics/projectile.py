import pygame

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        """
        Initialize a Projectile object.

        Args:
            x (int): The x-coordinate of the projectile's position.
            y (int): The y-coordinate of the projectile's position.
            radius (int): The radius of the projectile.
            color (tuple): The color of the projectile in RGB format.
            facing (int): The direction the projectile is facing (-1 for left, 1 for right).

        Returns:
            None
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):
        """
        Draw the projectile on the given window.

        Args:
            win (pygame.Surface): The window surface to draw the projectile on.

        Returns:
            None
        """
        pygame.draw.circle(win, self.color, (self.x, self.y - 23), self.radius)
