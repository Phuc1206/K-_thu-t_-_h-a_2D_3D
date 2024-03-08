import pygame
import math
import random
from config import*
from shapes import *

# Define colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (241, 255, 38)
DA=(255,255,204)
JEAN=(0,51,102)
BLACK=(0,0,0)

class Seat:
    def __init__(self, x, y, length, swing_width, speed, scale):
        self.x = x+20
        self.y = y
        self.length = length
        self.swing_width = swing_width
        self.angle = random.uniform(-math.pi / 4, math.pi / 4)
        self.speed = speed
        self.scale = scale+0.5
    
    def draw(self, window, y_stand):
        # Calculate the ends of the swing
        end_x_left = self.x - self.swing_width / 2 + self.length * math.sin(self.angle)
        end_y_left = y_stand + self.length * math.cos(self.angle)
        
        end_x_right = self.x + self.swing_width / 2 + self.length * math.sin(self.angle)
        end_y_right = y_stand + self.length * math.cos(self.angle)
        
        # Draw the swing chains
        draw_line(window, hong1, (self.x - self.swing_width / 2, y_stand), (end_x_left, end_y_left),1.5)
        draw_line(window, hong1, (self.x + self.swing_width / 2, y_stand), (end_x_right, end_y_right),1.5)
        
        # Draw the swing seat
        draw_ellipse_filled(window, xanh1, (end_x_left, end_y_left - 5, self.swing_width, 10))
        
        # Draw the person
        self.draw_person(window, (end_x_left + end_x_right) / 2, (end_y_left + end_y_right) / 2)

    def draw_person(self, window, x, y):
        # Draw the head
        draw_circle_filled(window, da, (int(x), int(y - 20 * self.scale)), int(10 * self.scale))
        
        # Draw the hands
        draw_filled_rect(window, vang, (x - 18 * self.scale, y - 10 * self.scale, 15 * self.scale, 5 * self.scale)) # left hand
        draw_filled_rect(window, vang, (x + 3 * self.scale, y - 10 * self.scale, 15 * self.scale, 5 * self.scale)) # right hand

        # Draw the body
        draw_filled_rect(window, cam, (x - 5 * self.scale, y - 10 * self.scale, 10 * self.scale, 20 * self.scale))

        # Draw the legs
        draw_line(window, xanh2, (x - 3 * self.scale, y + 10 * self.scale), (x - 3 * self.scale, y + 20 * self.scale), 2)
        draw_line(window, xanh2, (x + 3 * self.scale, y + 10 * self.scale), (x + 3 * self.scale, y + 20 * self.scale), 2)

    def update(self):
        self.angle += self.speed
        if self.angle > math.pi / 4:
            self.speed = -0.01
        elif self.angle < -math.pi / 4:
            self.speed = 0.01
class Swing:
    def __init__(self, x, y, length, swing_width, stand_height, stand_width, spacing):
        self.x = x
        self.y = y
        self.stand_height = stand_height
        self.stand_width = stand_width
        self.seats = [Seat(x + (swing_width + spacing) * i, y, length, swing_width, 0.01, 0.6) for i in range(3)]
        self.font = pygame.font.Font(None, 24)
        self.show_label = False
        self.zoom_level = 1
    def draw(self, window):
        # Draw the horizontal stand
        draw_line(window, WHITE, (self.x, self.y - self.stand_height), (self.x + self.stand_width, self.y - self.stand_height), 2)
        draw_line(window, xanh1, (self.x + self.stand_width, self.y), (self.x + self.stand_width, self.y - self.stand_height), 2)
        
        for seat in reversed(self.seats):
            seat.draw(window, self.y - self.stand_height)

        # Draw the stands
        draw_line(window, xanh1, (self.x, self.y), (self.x, self.y - self.stand_height), 2)
        
        # Draw the label
        if self.show_label:
            self.draw_label(window)
    def zoom(self, scale):
        self.stand_height *= scale
        self.stand_width *= scale
        for seat in self.seats:
            seat.length *= scale
            seat.swing_width *= scale
            seat.scale *= scale
    def draw_label(self, window):
        # Calculate the real coordinates of the first seat
        seat = self.seats[0]
        end_x_left = seat.x - seat.swing_width / 2 + seat.length * math.sin(seat.angle)
        end_y_left = self.y - self.stand_height + seat.length * math.cos(seat.angle)
        
        end_x_right = seat.x + seat.swing_width / 2 + seat.length * math.sin(seat.angle)
        end_y_right = self.y - self.stand_height + seat.length * math.cos(seat.angle)
        
        x = (end_x_left + end_x_right) / 2
        y = (end_y_left + end_y_right) / 2

        # Create the label surface
        label = self.font.render(f" ({x:.2f}, {y:.2f})", True, (255, 255, 255))
        
        # Draw the label on the window
        window.blit(label, (x,y))

    def update(self):
        for seat in self.seats:
            seat.update()
    def collidepoint(self, point):
    # Check if the point is within the horizontal stand
        if self.x <= point[0] <= self.x + self.stand_width and self.y - self.stand_height <= point[1] <= self.y:
            return True
    # The point is not within the swing
        return False
