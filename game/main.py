from collections.abc import KeysView
from pygame.locals import *
import pygame
import random
import sys
import assets
from settings import SCREEN_WIDTH
pygame.init()

screenWidht = 928
screenHeight = 643

icon = pygame.image.load("resources/sprites/icon/robe5.png")
pygame.display.set_icon(icon)

win = pygame.display.set_mode((screenWidht, screenHeight))
pygame.display.set_caption("Forest hunter")
fontObj = pygame.font.Font('resources/fonts/Frikativ.ttf', 50)

bg = pygame.image.load("resources/sprites/bg/gameBg.png")
mainMenuBg = pygame.image.load("resources/sprites/bg/mainMenuBg.png")

sprites = assets.load_sprites()


mainClock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)


sounds = assets.load_sounds()

hitSound = sounds['hit_sound']
music = sounds['background_music']
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(loops=-1)


class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.isJump = False
        self.left = False
        self.right = False
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

        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if self.coat + 1 >= 24:
            self.coat = 0

        if not (self.standing):
            if self.left:
                win.blit(
                    self.heroWalkLeft[self.walkCount//3], (self.x, self.y))
                win.blit(self.heroCoatLeft[self.coat//3], (self.x, self.y))
                win.blit
                self.walkCount += 1
                self.coat += 1
            elif self.right:
                win.blit(
                    self.heroWalkRight[self.walkCount//3], (self.x, self.y))
                win.blit(self.heroCoatRight[self.coat//3], (self.x, self.y))
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
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # HITBOX

    def hit(self):
        self.isJump = False
        self.jumpCount = 11
        self.x = random.randrange(screenWidht//2 - 100)
        self.y = 528
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (((screenWidht/2) - (text.get_width()/2)), 200))

        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):

        pygame.draw.circle(win, self.color, (self.x, self.y-23), self.radius)


class Enemy():
    def __init__(self, x, y, enemy_width, enemy_height,  end, hitbox_width, hitbox_height, enemyType='first', health=10):
        self.x = x
        self.y = y
        self.width = enemy_width
        self.height = enemy_height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x, self.y, hitbox_width, hitbox_height)
        self.health = health
        self.start_health = health
        self.visible = True
        self.enemyType = enemyType
        self.enemy_sprites = sprites[self.enemyType]
        self.walkRight = self.enemy_sprites['right']
        self.walkLeft = self.enemy_sprites['left']
        self.hitbox_width = hitbox_width
        self.hitbox_height = hitbox_height

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 24:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 7, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(
                win, (0, 128, 0), (self.hitbox[0] + 7, self.hitbox[1] - 20, 50 - (1 * (50 - self.health)), 10))
            self.hitbox = (self.x, self.y, self.hitbox_width,
                           self.hitbox_height)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # HITBOX

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        # print('hit')

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
            for bullet in bullets:
                bullets.remove(bullet)

        pass


def redrawGameWindow():
    global bullets
    win.blit(bg, (0, -150))  # y = -150
    text = font.render('Score: ' + str(score), 1, (45, 84, 145))
    bulletsLeft = font.render(
        "Bullets left " + str(bulletsCountLeft) + "  /  " + str(allBullets), 1, (45, 84, 145))
    win.blit(text, ((screenWidht - 150), 10))
    win.blit(bulletsLeft, ((screenWidht - 500), 10))
    man.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    textobj = fontObj.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


global click
click = False


def fade():
    fade = pygame.Surface((screenWidht, screenHeight))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        win.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(7)


def fadeStart():
    fadeStart = pygame.Surface((screenWidht, screenHeight))
    fadeStart.fill((0, 0, 0))
    for alpha in range(255, 0, -5):
        fadeStart.set_alpha(alpha)
        win.blit(mainMenuBg, (0, 0))
        draw_text('main menu', fontObj, (255, 255, 255),
                  win, screenWidht / 2 - 137, 72)
        draw_text('Play!', fontObj, (255, 255, 255),
                  win, screenWidht/2 - 56, 165)
        draw_text('Credits', fontObj, (255, 255, 255),
                  win, screenWidht/2 - 92, 266)
        draw_text('Exit', fontObj, (255, 255, 255), win, screenWidht/2-43, 366)
        win.blit(fadeStart, (0, 0))
        pygame.display.update()
        pygame.event.pump()


global fontObj1
fontObj1 = pygame.font.SysFont('comicsans', 30, True)


def credits():
    running = True

    while running:
        win.fill((0, 0, 0))

        draw_text('Credits', fontObj1, (255, 255, 255),
                  win, screenWidht/2 - 80, 50)
        draw_text('Created by Mihails Danilovs', fontObj1, (255, 255,
                  255), win, screenWidht/2 - 325, screenHeight/2 - 100)
        draw_text('md22039', fontObj1, (255, 255, 255), win,
                  screenWidht/2 - 115, screenHeight/2 + 50)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                fade()

                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fade()
                    running = False

        pygame.display.update()
        mainClock.tick(24)


global enemyPick, score


def main_menu():
    fadeStart()

    main_menuRunning = True
    global click
    while main_menuRunning:

        win.blit(mainMenuBg, (0, 0))
        draw_text('main menu', fontObj, (255, 255, 255),
                  win, screenWidht / 2 - 137, 72)
        draw_text('Play!', fontObj, (255, 255, 255),
                  win, screenWidht/2 - 56, 165)
        draw_text('Credits', fontObj, (255, 255, 255),
                  win, screenWidht/2 - 92, 266)
        draw_text('Exit', fontObj, (255, 255, 255), win, screenWidht/2-43, 366)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(314, 150, 300, 75)
        button_2 = pygame.Rect(314, 250, 300, 75)
        button_3 = pygame.Rect(314, 350, 300, 75)

        if button_1.collidepoint((mx, my)):
            if click:
                fade()
                game()

        if button_2.collidepoint((mx, my)):
            if click:
                fade()
                credits()
                fadeStart()
                global fontObj1
                fontObj1 = pygame.font.SysFont('comicsans', 30, True)

        if button_3.collidepoint((mx, my)):
            if click:
                fade()
                run = False
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
                fade()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fade()
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(24)

# mainloop


# !TODO Change to 1 after testing
enemyPick = 3
score = 0
font = pygame.font.SysFont('comicsans', 30, True)
bulletsCountLeft = 5
allBullets = 695


def game():
    global enemyPick, score, bulletsCountLeft, allBullets, bullets, enemy, man
    bullets = []

    shootLoop = 0

    # Randomly choosen spawn points within these ranges
    player_spawn_range = (50, SCREEN_WIDTH // 4)
    enemy_spawn_range = [SCREEN_WIDTH // 4 + 100, SCREEN_WIDTH - 200]
    player_x = random.randrange(*player_spawn_range)
    enemy_x = random.randrange(*enemy_spawn_range)
    enemyPathInPx = enemy_x + 200

    man = Player(player_x, 528, 64, 64)
    # Enemy can be created with the following parameters:
    # Enemy(x, y, enemy_width, enemy_height,  end, hitbox_width, hitbox_height, enemyType='first',health = 10):

    if enemyPick == 1:
        enemy = Enemy(enemy_x, 530, 64, 64, enemyPathInPx, 33, 58, 'first', 10)

    elif enemyPick == 2:
        enemy = Enemy(enemy_x, 530, 90, 90, enemyPathInPx,
                      120, 100, 'second', 20)
    elif enemyPick == 3:
        enemy = Enemy(enemy_x, 490, 90, 90, enemyPathInPx, 57, 90, 'third', 30)

    elif enemyPick == 4:
        enemy = Enemy(enemy_x, 490, 90, 90,
                      enemyPathInPx, 80, 100, 'fourth', 50)
    elif enemyPick == 5:
        enemy = Enemy(enemy_x, 490, 90, 90,
                      enemyPathInPx, 64, 120, 'fifth', 75)
    elif enemyPick >= 6:
        enemy = Enemy(enemy_x, 490, 90, 90,
                      enemyPathInPx, 64, 120, 'sixth', 100)

    run = True
    while run:
        mainClock.tick(30)

        if score < 0:
            # win.fill(255,255,255)
            allBullets = 695
            enemyPick = 0
            score = 0
            fade()
            # pygame.time.delay(3000)
            run = False

        if enemy.visible == True:
            if man.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and man.hitbox[1] + man.hitbox[3] > enemy.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > enemy.hitbox[0] and man.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                    man.hit()
                    score -= 5

        else:
            enemyPick += 1
            run = False

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fade()
                pygame.quit()
                sys.exit()

        for bullet in bullets:
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                if enemy.visible == True:
                    if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                        hitSound.play()
                        enemy.hit()
                        score += 1
                        bulletsCountLeft -= 1
                        if bullet in bullets:
                            bullets.remove(bullet)

            if bulletsCountLeft == 0:
                allBullets -= 5
                bulletsCountLeft = 5
            if bullet.x < screenWidht and bullet.x > 0:
                bullet.x += bullet.vel

            else:
                bullets.pop(bullets.index(bullet))
                bulletsCountLeft -= 1
                bulletsCountLeft = 5

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:

            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:
                bullets.append(projectile(round(man.x + man.width // 2),
                               round(man.y + man.height//2), 3, (255, 255, 255), facing))
                shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False

        elif keys[pygame.K_RIGHT] and man.x < screenWidht - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False

        else:
            man.standing = True
            man.walkCount = 0

        if not (man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0

        else:
            if man.jumpCount >= -11:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 11

        redrawGameWindow()


main_menu()
pygame.quit()
