import pygame, pygame.gfxdraw
import time

screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
screen.fill((0, 0, 0))
pygame.gfxdraw.circle(screen, 400, 300, 200, (255, 255, 255))
pygame.display.flip()

time.sleep()