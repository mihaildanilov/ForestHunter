# entity_initialization.py

import random
from entities.player import Player
from entities.enemy import Enemy
from settings import SCREEN_WIDTH

def initialize_entities(enemyPick, sprites):
    """
    Initializes the player and enemy entities.

    Args:
    - enemyPick (int): The type of enemy to initialize.
    - sprites (dict): A dictionary containing the sprites for the entities.

    Returns:
    - man (Player): The initialized player entity.
    - enemy (Enemy): The initialized enemy entity.
    """
    player_spawn_range = [50, 100]
    enemy_spawn_range = [120, SCREEN_WIDTH - 200]
    player_x = random.randrange(*player_spawn_range)
    enemy_x = random.randrange(*enemy_spawn_range)
    enemyPathInPx = enemy_x + 200

    man = Player(player_x, 528, 64, 64, sprites)

    if enemyPick == 1:
        enemy = Enemy(enemy_x, 530, 64, 64, enemyPathInPx, 33, 58, sprites, 'first', 10)
    elif enemyPick == 2:
        enemy = Enemy(enemy_x, 490, 90, 90, enemyPathInPx, 120, 100, sprites, 'second', 20)
    elif enemyPick == 3:
        enemy = Enemy(enemy_x, 490, 90, 90, enemyPathInPx, 57, 90, sprites, 'third', 30)
    elif enemyPick == 4:
        enemy = Enemy(enemy_x, 490, 90, 90, enemyPathInPx, 80, 100, sprites, 'fourth', 50)
    elif enemyPick == 5:
        enemy = Enemy(enemy_x, 490, 90, 90, enemyPathInPx, 64, 120, sprites, 'fifth', 75)
    elif enemyPick >= 6:
        enemy = Enemy(enemy_x, 490, 90, 90, enemyPathInPx, 64, 120, sprites, 'sixth', 100)

    return man, enemy
