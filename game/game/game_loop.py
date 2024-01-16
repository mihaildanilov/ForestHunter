import pygame
import sys
from utils.entity_initialization import initialize_entities
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.utility_functions import fade, redrawGameWindow
from mechanics.projectile import Projectile
from init_game import win, mainClock, comicsans, bg, sprites, hitSound


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

    man, enemy = initialize_entities(enemyPick, sprites)
    run = True
    while run:
        mainClock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fade(win)
                pygame.quit()
                sys.exit()

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
