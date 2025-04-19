import pygame
import os
from random import *
pygame.init()

size_window = (600, 700)
size_background = (600, 3000)
size_hero = (100, 100)
size_bot = (75, 75)
size_buff = (50, 50)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED= (255, 0 ,0)
FPS = 60
BLUE = (0, 0, 255)
count_buff = 5
BUFFS = ["HP", "speed_bullet", "speed_shoot", "imortal", "freezing"]
heart_list = list()
ticket_list = list()
bot_list = list()
bullet_list_hero = list()
bullet_list_bot = list()


abs_path = os.path.abspath(__file__ + "/..")
hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "Hero_fly.png")), size_hero)
]
bot_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "PLANE_ENEMY.png")), size_bot),
    
]

skull_image_list = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "skull.png")), size_bot)
heart_image_list = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "heart.png")), size_bot)
background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "fon_norm.png")), size_background)
buff_images = [
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_heart.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_speedbullet.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_speedshoot.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_imortality.png")), size_buff),
pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "b_freez.png")), size_buff)
]


