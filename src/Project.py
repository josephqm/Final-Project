import os 
import random 
import math 
import pygame
from os import listdir
from os.path import isfile, join 
pygame.init()

pygame.display.set_caption("Final Project Joseph Monroe")

BACKGROUND_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800

FPS = 60
PLAYER_VELOCITY = 5

window