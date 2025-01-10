# rendering.py
import pygame
from constants import BALL_IMAGE_PATH, PADDLE_IMAGE_PATH, BACKGROUND_IMAGE_PATH

# Memuat aset visual
ball_image = pygame.image.load(BALL_IMAGE_PATH)
paddle_image = pygame.image.load(PADDLE_IMAGE_PATH)
background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)

def render_background(screen):
    # Render latar belakang
    screen.blit(background_image, (0, 0))

def render_ball(screen, ball_x, ball_y):
    # Render bola
    ball_rect = ball_image.get_rect(center=(ball_x, ball_y))
    screen.blit(ball_image, ball_rect)

def render_paddle(screen, paddle_x, paddle_y):
    # Render paddle
    paddle_rect = paddle_image.get_rect(topleft=(paddle_x, paddle_y))
    screen.blit(paddle_image, paddle_rect)
