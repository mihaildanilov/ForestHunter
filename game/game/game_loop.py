import pygame
import sys
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from utils import fade, redrawGameWindow
from mechanics.projectile import Projectile
from entities.enemy import Enemy
from init_game import win, mainClock, comicsans, bg, sprites, hitSound
from entities.player import Player


def game_loop(enemyPick, score, bulletsCountLeft, allBullets):
    """
    The main game loop that handles the gameplay logic.

    Args:
        enemyPick (int): The enemy type to spawn.
        score (int): The current score.
        bulletsCountLeft (int): The number of bullets left.
        allBullets (int): The total number of bullets.

    Returns:
        enemyPick (int): The updated enemy type to spawn.
        score (int): The updated score.
        bulletsCountLeft (int): The updated number of bullets left.
        allBullets (int): The updated total number of bullets.
    """
    bullets = []
    shootLoop = 0

    # Randomly choosen spawn points within these ranges
    player_spawn_range = (50, SCREEN_WIDTH // 4)
    enemy_spawn_range = [SCREEN_WIDTH // 4 + 100, SCREEN_WIDTH - 200]
    player_x = random.randrange(*player_spawn_range)
    enemy_x = random.randrange(*enemy_spawn_range)
    enemyPathInPx = enemy_x + 200

    man = Player(player_x, 528, 64, 64, sprites)

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
            allBullets = 695
            enemyPick = 1
            score = 0
            fade(win)
            run = False

        if enemy.visible:
            if man.hitbox[1] < enemy.hitbox[1] + \
                    enemy.hitbox[3] and man.hitbox[1] + man.hitbox[3] > enemy.hitbox[1]:
                if man.hitbox[0] + \
                        man.hitbox[2] > enemy.hitbox[0] and man.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
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
                fade(win)
                pygame.quit()
                sys.exit()

        for bullet in bullets:
            if bullet.y - \
                    bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                if enemy.visible:
                    if bullet.x + \
                            bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
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

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:
                bullets.append(
                    Projectile(
                        round(
                            man.x +
                            man.width //
                            2),
                        round(
                            man.y +
                            man.height //
                            2),
                        3,
                        (255,
                         255,
                         255),
                        facing))
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

        redrawGameWindow(win, comicsans, score, bulletsCountLeft,
                         allBullets, man, enemy, bullets, bg)

    return enemyPick, score, bulletsCountLeft, allBullets
