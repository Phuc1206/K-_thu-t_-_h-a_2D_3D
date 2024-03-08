import pygame
import math
from shapes import *

class Background:
    def __init__(self):
        self.rectangles = []
        self.circles = []
    def add_circle(self, x, y, radius, color):
        self.circles.append((x, y, radius, color))

    def draw_circle(self, surface, circle):
        x, y, radius, color = circle

        # Sử dụng pygame.draw.circle để vẽ hình tròn có màu
        pygame.draw.circle(surface, color, (x, y), radius)

    def add_rounded_rect(self, x, y, width, height, stairs, color, radius):
        self.rectangles.append((x, y, width, height, stairs, color, radius))

    def draw_rounded_rect(self, surface, rect):
        x, y, width, height, stairs, color, radius = rect

        pygame.draw.rect(surface, color, (x + radius, y, width - 2 * radius, height))
        pygame.draw.rect(surface, color, (x, y + radius, width, height - 2 * radius))

        pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
        pygame.draw.circle(surface, color, (x + width - radius, y + radius), radius)
        pygame.draw.circle(surface, color, (x + radius, y + height - radius), radius)
        pygame.draw.circle(surface, color, (x + width - radius, y + height - radius), radius)

    def draw_background(self, surface):
        for rectangle in self.rectangles:
            self.draw_rounded_rect(surface, rectangle)

        for circle in self.circles:
            self.draw_circle(surface, circle)