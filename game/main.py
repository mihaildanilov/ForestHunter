from pygame.locals import *
import pygame
import random
import sys
import assets
from enemy import Enemy
from game_functions import redrawGameWindow
from player import Player
from projectile import Projectile
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = assets.load_image("sprites/icon/robe5.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Forest hunter")

main_font = assets.load_fonts()['main_font']
comicsans = assets.load_fonts()['comicsans']

bg = assets.load_image("sprites/bg/gameBg.png")
mainMenuBg = assets.load_image("sprites/bg/mainMenuBg.png")

sprites = assets.load_sprites()

mainClock = pygame.time.Clock()

sounds = assets.load_sounds()
hitSound = sounds['hit_sound']
music = sounds['background_music']
pygame.mixer.music.set_volume(0.01)
hitSound.set_volume(0.01)
pygame.mixer.music.play(loops=-1)

enemyPick = 1
score = 0
bulletsCountLeft = 5
allBullets = 695
click = False




def draw_text(text, font, color, surface, x, y):
    obj = font.render(text, 1, color)
    rect = obj.get_rect()
    rect.topleft = (x, y)
    surface.blit(obj, rect)


def fade():
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        win.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(7)


def fadeStart():
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


def credits():
    running = True

    while running:
        win.fill((0, 0, 0))

        draw_text('Credits', comicsans, (255, 255, 255),
                  win, SCREEN_WIDTH/2 - 40, 50)
        draw_text('Created by Mihails Danilovs', comicsans, (255, 255,
                  255), win, SCREEN_WIDTH/2 - 190, SCREEN_HEIGHT/2 - 100)
        draw_text('md22039', comicsans, (255, 255, 255), win,
                  SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2 - 30)

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


def main_menu():
    fadeStart()
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
                fade()
                game()

        if button_2.collidepoint((mx, my)):
            if click:
                fade()
                credits()
                fadeStart()

        if button_3.collidepoint((mx, my)):
            if click:
                fade()
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

    man = Player(player_x, 528, 64, 64, sprites)
    # Enemy can be created with the following parameters:
    # Enemy(x, y, enemy_width, enemy_height,  end, hitbox_width, hitbox_height, enemyType='first',health = 10):

    if enemyPick == 1:
        enemy = Enemy(enemy_x, 530, 64, 64, enemyPathInPx,
                      33, 58, sprites, 'first', 10)

    elif enemyPick == 2:
        enemy = Enemy(enemy_x, 490, 90, 90, enemyPathInPx,
                      120, 100, sprites, 'second', 20)
    elif enemyPick == 3:
        enemy = Enemy(enemy_x, 490, 90, 90, enemyPathInPx,
                      57, 90, sprites, 'third', 30)

    elif enemyPick == 4:
        enemy = Enemy(enemy_x, 490, 90, 90,
                      enemyPathInPx, 80, 100, sprites, 'fourth', 50)
    elif enemyPick == 5:
        enemy = Enemy(enemy_x, 490, 90, 90,
                      enemyPathInPx, 64, 120, sprites, 'fifth', 75)
    elif enemyPick >= 6:
        enemy = Enemy(enemy_x, 490, 90, 90,
                      enemyPathInPx, 64, 120, sprites, 'sixth', 100)

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
                    man.hit(win)
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
                        enemy.hit(bullets)
                        score += 1
                        bulletsCountLeft -= 1
                        if bullet in bullets:
                            bullets.remove(bullet)

            if bulletsCountLeft == 0:
                allBullets -= 5
                bulletsCountLeft = 5
            if bullet.x < SCREEN_WIDTH and bullet.x > 0:
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
                bullets.append(Projectile(round(man.x + man.width // 2),
                               round(man.y + man.height//2), 3, (255, 255, 255), facing))
                shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False

        elif keys[pygame.K_RIGHT] and man.x < SCREEN_WIDTH - man.width - man.vel:
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

        redrawGameWindow(win,comicsans,score,bulletsCountLeft,allBullets,man,enemy,bullets,bg)


main_menu()
pygame.quit()
