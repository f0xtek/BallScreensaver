import sys

import pygame
from pygame.locals import *

from ball import Ball

if __name__ == '__main__':
    BLACK = (0, 0, 0)
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 960
    FPS = 30
    NUM_BALLS = 10

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    ball_list = []
    for i in range(NUM_BALLS):
        ball = Ball(window=window, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT)
        ball_list.append(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for ball in ball_list:
            ball.update()
        window.fill(BLACK)
        for ball in ball_list:
            ball.draw()
        pygame.display.update()
        clock.tick(FPS)
