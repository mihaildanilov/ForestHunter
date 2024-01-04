# assets.py
import pygame
import os

# Path to the resources directory
RESOURCES_DIR = os.path.join(os.path.dirname(__file__), '..', 'resources')


def load_image(path):
    full_path = os.path.join(RESOURCES_DIR, path)
    if os.path.exists(full_path):
        return pygame.image.load(full_path).convert_alpha()
    else:
        raise FileNotFoundError(f"Unable to find {full_path}")


def load_sound(path):
    full_path = os.path.join(RESOURCES_DIR, path)
    if os.path.exists(full_path):
        return pygame.mixer.Sound(full_path)
    else:
        raise FileNotFoundError(f"Unable to find {full_path}")
    
def load_music(path):
    full_path = os.path.join(RESOURCES_DIR, path)
    if os.path.exists(full_path):
        return pygame.mixer.music.load(full_path)
    else:
        raise FileNotFoundError(f"Unable to find {full_path}")    


def load_font(path, size):
    full_path = os.path.join(RESOURCES_DIR, path)
    if os.path.exists(full_path):
        return pygame.font.Font(full_path, size)
    else:
        raise FileNotFoundError(f"Unable to find {full_path}")


def load_sprites_from_folder(folder, extension="png", num_sprites=8):
    sprites = []
    for i in range(num_sprites):
        path = f"{folder}/tile00{i}.{extension}"
        sprites.append(load_image(path))
    return sprites


def load_sprites():
    hero_sprites = {
        'right': load_sprites_from_folder('sprites/hero/RIGHT', num_sprites=8),
        'left': load_sprites_from_folder('sprites/hero/LEFT', num_sprites=8),
        'standing-right': load_image('sprites/hero/RIGHT/standingR.png'),
        'standing-left': load_image('sprites/hero/LEFT/standingL.png'),
        'coat-right': load_sprites_from_folder('sprites/coat/RIGHT', num_sprites=8),
        'coat-left': load_sprites_from_folder('sprites/coat/LEFT', num_sprites=8),
        'standing-coat-right': load_image('sprites/coat/RIGHT/standingCoatR.png'),
        'standing-coat-left': load_image('sprites/coat/LEFT/standingCoatL.png')
    }
    first_enemy = {
        'right': load_sprites_from_folder('sprites/enemies/firstEnemy/RIGHT', num_sprites=8),
        'left': load_sprites_from_folder('sprites/enemies/firstEnemy/LEFT', num_sprites=8)
    }
    second_enemy = {
        'right': load_sprites_from_folder('sprites/enemies/secondEnemy/RIGHT', num_sprites=10),
        'left': load_sprites_from_folder('sprites/enemies/secondEnemy/LEFT', num_sprites=10)
    }
    third_enemy = {
        'right': load_sprites_from_folder('sprites/enemies/thirdEnemy/RIGHT', num_sprites=8),
        'left': load_sprites_from_folder('sprites/enemies/thirdEnemy/LEFT', num_sprites=8)
    }
    fourth_enemy = {
        'right': load_sprites_from_folder('sprites/enemies/fourthEnemy/RIGHT', num_sprites=8),
        'left': load_sprites_from_folder('sprites/enemies/fourthEnemy/LEFT', num_sprites=8)
    }
    fifth_enemy = {
        'right': load_sprites_from_folder('sprites/enemies/fifthEnemy/RIGHT', num_sprites=8),
        'left': load_sprites_from_folder('sprites/enemies/fifthEnemy/LEFT', num_sprites=8)
    }
    sixth_enemy = {
        'right': load_sprites_from_folder('sprites/enemies/sixthEnemy/RIGHT', num_sprites=16),
        'left': load_sprites_from_folder('sprites/enemies/sixthEnemy/LEFT', num_sprites=16)
    }

    return {
        'hero': hero_sprites,
        'first': first_enemy,
        'second': second_enemy,
        'third': third_enemy,
        'fourth': fourth_enemy,
        'fifth': fifth_enemy,
        'sixth': sixth_enemy
    }


def load_fonts():
    frikativ = load_font('fonts/Frikativ.ttf', 20)
    sys_font = pygame.font.SysFont('comicsans', 30, True)
    return {
        'main_font': frikativ,
        'sys_font': sys_font
    }


def load_sounds():
    background_music = load_music('sounds/background_music.mp3')
    hit_sound = load_sound('sounds/hit.ogg')

    return {
        'background_music': background_music,
        'hit_sound': hit_sound
    }
