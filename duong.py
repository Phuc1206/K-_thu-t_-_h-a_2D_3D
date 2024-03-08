import pygame
import pygame.gfxdraw
import numpy as np
import math


# Màu sắc
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)  # Màu của đèn đường

# Lớp StreetLamp (đèn đường)
class StreetLamp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lamp_radius = 10  # Bán kính của đèn
        self.post_height = 50  # Chiều cao của cột đèn
        self.post_width = 5  # Độ rộng của cột đèn

    def draw(self, screen):
        # Vẽ cột đèn bằng một hình chữ nhật
        pygame.draw.rect(screen, GRAY, (self.x - self.post_width // 2, self.y, self.post_width, self.post_height))

        # Vẽ đèn bằng một hình tròn
        pygame.gfxdraw.aacircle(screen, self.x, self.y, self.lamp_radius, YELLOW)
        pygame.gfxdraw.filled_circle(screen, self.x, self.y, self.lamp_radius, YELLOW)

# Tính toán điểm trên đường cong Bézier từ bốn điểm và một tham số t
def bezier_curve(t, points):
    return ((1 - t)**3 * points[0][0] + 3 * (1 - t)**2 * t * points[1][0] + 3 * (1 - t) * t**2 * points[2][0] + t**3 * points[3][0],
            (1 - t)**3 * points[0][1] + 3 * (1 - t)**2 * t * points[1][1] + 3 * (1 - t) * t**2 * points[2][1] + t**3 * points[3][1])

class Bench:
    def __init__(self, x, y, angle=0, width=60, height=20, leg_width=5, leg_height=10):
        self.x = x
        self.y = y
        self.angle = math.radians(angle)  # Convert angle to radians
        self.width = width
        self.height = height
        self.leg_width = leg_width
        self.leg_height = leg_height

    def draw(self, screen):
        # Calculate the four corners of the rotated rectangle
        corners = [(self.x + dx * math.cos(self.angle) - dy * math.sin(self.angle),
                    self.y + dx * math.sin(self.angle) + dy * math.cos(self.angle))
                   for dx, dy in [(0, 0), (self.width, 0), (self.width, self.height), (0, self.height)]]

        # Draw the seat of the bench
        pygame.draw.polygon(screen, (139, 69, 19), corners)

        # Draw the legs of the bench
        x, y = corners[0]
        pygame.draw.rect(screen, (139, 69, 19), (x, y+3, self.leg_width, self.leg_height))
        x1, y1 = corners[1]
        pygame.draw.rect(screen, (139, 69, 19), (x1 - 4, y1+3, self.leg_width, self.leg_height))
        pygame.draw.rect(screen, (139, 69, 19), (*corners[3], self.leg_width, self.leg_height))
        x2, y2 = corners[2]
        pygame.draw.rect(screen, (139, 69, 19), (x2 - 4, y2, self.leg_width, self.leg_height))

class CircularFence:
    def __init__(self, x, y, radius, num_posts, num_lamps, post_height, post_width):
        self.x = x
        self.y = y
        self.radius = radius
        self.num_posts = num_posts
        self.num_lamps = num_lamps
        self.post_height = post_height
        self.post_width = post_width
        self.street_lamps = self.create_street_lamps()

    def create_street_lamps(self):
        street_lamps = []
        # Calculate the angle between each lamp
        angle_step = 2 * math.pi / self.num_lamps

        # Create each lamp
        for i in range(self.num_lamps):
            angle = i * angle_step
            lamp_x = self.x + self.radius * math.cos(angle)
            lamp_y = self.y + self.radius * math.sin(angle)
            street_lamps.append(StreetLamp(int(lamp_x), int(lamp_y)))
        return street_lamps

    def draw(self, screen):
        # Calculate the angle between each post
        angle_step = 2 * math.pi / self.num_posts

        # Create a list to store the coordinates of the post tops
        post_tops = []

        # Draw each post
        for i in range(self.num_posts):
            angle = i * angle_step
            post_x = self.x + self.radius * math.cos(angle)
            post_y = self.y + self.radius * math.sin(angle)
            pygame.draw.rect(screen, (139, 69, 19), (post_x, post_y, self.post_width, self.post_height))

            # Add the top of the post to the list
            post_tops.append((post_x, post_y))

        # Draw lines between the tops of the posts
        pygame.draw.lines(screen, (139, 69, 19), True, post_tops, self.post_width)
        
        # Draw the street lamps
        for lamp in self.street_lamps:
            lamp.draw(screen)

class Road:
    def __init__(self, bezier_points_1, bezier_points_2):
        self.bezier_points_1 = bezier_points_1
        self.bezier_points_2 = bezier_points_2
        self.num_lamps = 5  # Số lượng đèn đường trên mỗi đường cong
        self.post_height = 100
        self.street_lamps = []

        # Tạo một chiếc ghế duy nhất với các thông số cụ thể
        t = 0.5  # Tham số t cho đường cong Bézier
        point = bezier_curve(t, self.bezier_points_1)
        self.bench = Bench(60, 400, angle=-10, width=60, height=20)
        self.bench2 = Bench(400, 310, angle=18, width=60, height=20)
        self.bench3 = Bench(750, 480, angle=-20, width=60, height=20)
        

    def draw(self, screen):
        # Vẽ mỗi đèn đường
        for lamp in self.street_lamps:
            lamp.draw(screen)

        # Vẽ chiếc ghế
        self.bench.draw(screen)
        self.bench2.draw(screen)
        self.bench3.draw(screen)

        # Vẽ đường cong Bézier
        for t in np.linspace(0, 1, 1000):
            point = bezier_curve(t, self.bezier_points_1)
            pygame.gfxdraw.pixel(screen, int(point[0]), int(point[1] + self.post_height), GRAY)
            point = bezier_curve(t, self.bezier_points_2)
            pygame.gfxdraw.pixel(screen, int(point[0]), int(point[1] + self.post_height), GRAY)