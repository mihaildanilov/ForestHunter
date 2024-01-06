import random
import pygame

from settings import SCREEN_WIDTH


class Player(object):
    """
    Represents the player character in the game.

    Attributes:
        x (int): The x-coordinate of the player's position.
        y (int): The y-coordinate of the player's position.
        width (int): The width of the player's sprite.
        height (int): The height of the player's sprite.
        vel (int): The velocity of the player's movement.
        isJump (bool): Indicates whether the player is currently jumping.
        left (bool): Indicates whether the player is facing left.
        right (bool): Indicates whether the player is facing right.
        walkCount (int): The count of frames for walking animation.
        coat (int): The count of frames for coat animation.
        jumpCount (int): The count of frames for jumping animation.
        standing (bool): Indicates whether the player is standing still.
        hitbox (tuple): The hitbox of the player's sprite.
        heroWalkRight (list): List of sprites for walking right.
        heroWalkLeft (list): List of sprites for walking left.
        heroCoatRight (list): List of sprites for walking right with coat.
        heroCoatLeft (list): List of sprites for walking left with coat.
        heroStandingR (Surface): Sprite for standing right.
        heroStandingL (Surface): Sprite for standing left.
        heroStandingCoatR (Surface): Sprite for standing right with coat.
        heroStandingCoatL (Surface): Sprite for standing left with coat.
    """

    def __init__(self, x, y, width, height, sprites):
        """
        Initializes a new instance of the Player class.

        Args:
            x (int): The initial x-coordinate of the player's position.
            y (int): The initial y-coordinate of the player's position.
            width (int): The width of the player's sprite.
            height (int): The height of the player's sprite.
            sprites (dict): A dictionary containing the player's sprites.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.isJump = False
        self.left = False
        self.right = True
        self.walkCount = 0
        self.coat = 0
        self.jumpCount = 11
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 5, 29, 51)
        # sprite loading
        hero_sprites = sprites['hero']
        self.heroWalkRight = hero_sprites['right']
        self.heroWalkLeft = hero_sprites['left']
        self.heroCoatRight = hero_sprites['coat-right']
        self.heroCoatLeft = hero_sprites['coat-left']
        self.heroStandingR = hero_sprites['standing-right']
        self.heroStandingL = hero_sprites['standing-left']
        self.heroStandingCoatR = hero_sprites['standing-coat-right']
        self.heroStandingCoatL = hero_sprites['standing-coat-left']

    def draw(self, win):
        """
        Draws the player's sprite on the game window.

        Args:
            win (Surface): The game window surface.

        Returns:
            None
        """
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if self.coat + 1 >= 24:
            self.coat = 0

        if not (self.standing):
            if self.left:
                win.blit(
                    self.heroWalkLeft[self.walkCount // 3], (self.x, self.y))
                win.blit(self.heroCoatLeft[self.coat // 3], (self.x, self.y))
                win.blit
                self.walkCount += 1
                self.coat += 1
            elif self.right:
                win.blit(
                    self.heroWalkRight[self.walkCount // 3], (self.x, self.y))
                win.blit(self.heroCoatRight[self.coat // 3], (self.x, self.y))
                self.walkCount += 1
                self.coat += 1
        else:
            if self.right:
                win.blit(self.heroStandingR, (self.x, self.y))
                win.blit(self.heroStandingCoatR, (self.x, self.y))
            else:
                win.blit(self.heroStandingL, (self.x, self.y))
                win.blit(self.heroStandingCoatL, (self.x, self.y))

        self.hitbox = (self.x, self.y, 40, 50)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # PLAYER HITBOX
        # comment to make invisible

    def hit(self, win):
        """
        Handles the player being hit.

        Args:
            win (Surface): The game window surface.

        Returns:
            None
        """
        self.isJump = False
        self.jumpCount = 11
        self.x = random.randrange(SCREEN_WIDTH // 2 - 100)
        self.y = 528
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (((SCREEN_WIDTH / 2) - (text.get_width() / 2)), 200))

        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
