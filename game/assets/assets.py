# assets.py
import pygame
import os

# Path to the resources directory
RESOURCES_DIR = os.path.join(os.path.dirname(__file__), '../..', 'resources')


def load_image(path):
    """
    Load an image from the specified path.

    Args:
        path (str): The path to the image file.

    Returns:
        pygame.Surface: The loaded image as a pygame Surface object.

    Raises:
        FileNotFoundError: If the image file cannot be found.
    """
    full_path = os.path.join(RESOURCES_DIR, path)
    if os.path.exists(full_path):
        return pygame.image.load(full_path).convert_alpha()
    else:
        raise FileNotFoundError(f"Unable to find {full_path}")


def load_sound(path):
    """
    Load a sound from the specified path.

    Args:
        path (str): The path to the sound file.

    Returns:
        pygame.mixer.Sound: The loaded sound as a pygame Sound object.

    Raises:
        FileNotFoundError: If the sound file cannot be found.
    """
    full_path = os.path.join(RESOURCES_DIR, path)
    if os.path.exists(full_path):
        return pygame.mixer.Sound(full_path)
    else:
        raise FileNotFoundError(f"Unable to find {full_path}")


def load_music(path):
    """
    Load music from the specified path.

    Args:
        path (str): The path to the music file.

    Returns:
        None

    Raises:
        FileNotFoundError: If the music file cannot be found.
    """
    full_path = os.path.join(RESOURCES_DIR, path)
    if os.path.exists(full_path):
        return pygame.mixer.music.load(full_path)
    else:
        raise FileNotFoundError(f"Unable to find {full_path}")


def load_font(path, size):
    """
    Load a font from the specified path.

    Args:
        path (str): The path to the font file.
        size (int): The size of the font.

    Returns:
        pygame.font.Font: The loaded font as a pygame Font object.

    Raises:
        FileNotFoundError: If the font file cannot be found.
    """
    full_path = os.path.join(RESOURCES_DIR, path)
    if os.path.exists(full_path):
        return pygame.font.Font(full_path, size)
    else:
        raise FileNotFoundError(f"Unable to find {full_path}")


def load_sprites_from_folder(folder, extension="png", num_sprites=8):
    """
    Load sprites from a folder.

    Args:
        folder (str): The path to the folder containing the sprites.
        extension (str, optional): The file extension of the sprites. Defaults to "png".
        num_sprites (int, optional): The number of sprites to load. Defaults to 8.

    Returns:
        list: A list of loaded sprites as pygame Surface objects.
    """
    sprites = []
    for i in range(num_sprites):
        path = f"{folder}/tile00{i}.{extension}"
        sprites.append(load_image(path))
    return sprites


def load_sprites():
    """
    Load all sprites used in the game.

    Returns:
        dict: A dictionary containing all the loaded sprites.
            The keys are the names of the sprite groups, and the values are dictionaries
            containing the sprites for each direction and state.
    """
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
        'right': load_sprites_from_folder(
            'sprites/enemies/firstEnemy/RIGHT',
            num_sprites=8),
        'left': load_sprites_from_folder(
            'sprites/enemies/firstEnemy/LEFT',
            num_sprites=8)}
    second_enemy = {
        'right': load_sprites_from_folder(
            'sprites/enemies/secondEnemy/RIGHT',
            num_sprites=10),
        'left': load_sprites_from_folder(
            'sprites/enemies/secondEnemy/LEFT',
            num_sprites=10)}
    third_enemy = {
        'right': load_sprites_from_folder(
            'sprites/enemies/thirdEnemy/RIGHT',
            num_sprites=8),
        'left': load_sprites_from_folder(
            'sprites/enemies/thirdEnemy/LEFT',
            num_sprites=8)}
    fourth_enemy = {
        'right': load_sprites_from_folder(
            'sprites/enemies/fourthEnemy/RIGHT',
            num_sprites=8),
        'left': load_sprites_from_folder(
            'sprites/enemies/fourthEnemy/LEFT',
            num_sprites=8)}
    fifth_enemy = {
        'right': load_sprites_from_folder(
            'sprites/enemies/fifthEnemy/RIGHT',
            num_sprites=8),
        'left': load_sprites_from_folder(
            'sprites/enemies/fifthEnemy/LEFT',
            num_sprites=8)}
    sixth_enemy = {
        'right': load_sprites_from_folder(
            'sprites/enemies/sixthEnemy/RIGHT',
            num_sprites=16),
        'left': load_sprites_from_folder(
            'sprites/enemies/sixthEnemy/LEFT',
            num_sprites=16)}

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
    """
    Load all fonts used in the game.

    Returns:
        dict: A dictionary containing all the loaded fonts.
            The keys are the names of the fonts, and the values are pygame Font objects.
    """
    frikativ = load_font('fonts/Frikativ.ttf', 50)
    comicsans = pygame.font.SysFont('comicsans', 30, True)
    return {
        'main_font': frikativ,
        'comicsans': comicsans
    }


def load_sounds():
    """
    Load all sounds used in the game.

    Returns:
        dict: A dictionary containing all the loaded sounds.
            The keys are the names of the sounds, and the values are the loaded sound objects.
    """
    background_music = load_music('sounds/background_music.mp3')
    hit_sound = load_sound('sounds/hit.ogg')

    return {
        'background_music': background_music,
        'hit_sound': hit_sound
    }
