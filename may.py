import pygame
import random
import math
from shapes import *
class MayBay:
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.tx = 2
        self.ty = 0
        self.animation_running = True
        self.font = pygame.font.Font(None, 24)
    def zoom(self, scale):
        self.width *= scale
        self.height *= scale
    def update(self):
        self.x += self.tx # phép tịnh tiến
        self.y += self.ty 
        if self.x > 800:  # Nếu mây bay đi ra ngoài màn hình bên phải, đặt lại tọa độ x và random tọa độ y để mây bay quay lại từ bên trái
            self.reset_position()
    def show_coordinates(self, window):
    # Display the coordinates
        label = self.font.render(f'({self.x:.1f}, {self.y:.1f})', True, (0, 255, 255))
        window.blit(label, (self.x, self.y))
    def draw_oval(self, screen, x, y, width, height): #vẽ hình oval
        num_points = 20
        points = []
        for i in range(num_points):
            angle = i * 2 * math.pi / num_points
            x_pos = x + width * 0.5 + width * 0.5 * math.cos(angle)
            y_pos = y + height * 0.5 + height * 0.5 * math.sin(angle)
            points.append((x_pos, y_pos))
        draw_polygon(screen, self.color, points,26)

    def draw(self, screen):
        # Vẽ 3 hình oval tạo thành hình dạng mây
        self.draw_oval(screen, self.x, self.y, self.width, self.height)
        self.draw_oval(screen, self.x + 20, self.y - 10, self.width + 20, self.height + 10)
        self.draw_oval(screen, self.x + 40, self.y, self.width + 20, self.height)
    def reset_position(self):
        self.x = -self.x+850 # phép đối xứng
        self.y = random.randint(50, 150)

    