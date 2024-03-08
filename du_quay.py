import pygame
import sys
import math
from config import*
import random
from shapes import *
# Khởi tạo Pygame
pygame.init()

# Thiết lập màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 204)
YELLOW = (241, 255, 38)
seat_colors = [xanh1,hong1,vang,xanhla,cam]
num_of_seats = 16
selected_colors = random.choices(seat_colors, k=num_of_seats)
class Carousel:
    def __init__(self, x, y, length_of_arm, num_of_arms, speed,
                 center_radius, base_arm_length, base_arm_width,
                 circle_radius, circle_radius_2, circle_radius_3,
                 spike_length, seat_width, seat_height, connection_radius, base_arm_width_2):
        self.x = x
        self.y = y
        self.length_of_arm = length_of_arm
        self.num_of_arms = num_of_arms
        self.speed = speed
        self.center_radius = center_radius
        self.base_arm_length = base_arm_length
        self.base_arm_width = base_arm_width
        self.circle_radius = circle_radius
        self.circle_radius_2 = circle_radius_2
        self.circle_radius_3 = circle_radius_3
        self.spike_length = spike_length
        self.seat_width = seat_width
        self.seat_height = seat_height
        self.connection_radius = connection_radius
        self.base_arm_width_2 = base_arm_width_2
        self.animation_running = True
        self.font = pygame.font.Font(None, 24)
    def zoom(self, scale):
        self.length_of_arm *= scale
        self.center_radius *= scale
        self.base_arm_length *= scale
        self.base_arm_width *= scale
        self.circle_radius *= scale
        self.circle_radius_2 *= scale
        self.circle_radius_3 *= scale
        self.spike_length *= scale
        self.seat_width *= scale
        self.seat_height *= scale
        self.connection_radius *= scale
        self.base_arm_width_2 *= scale
    def collidepoint(self, point):
        distance = math.sqrt((point[0] - self.x) ** 2 + (point[1] - self.y) ** 2)
        return distance <= self.circle_radius_3 + 50
    def show_coordinates(self, window):
        for i in range(self.num_of_arms):
            angle = i * 2 * math.pi / self.num_of_arms + self.speed
            end_x1 = self.length_of_arm * math.cos(angle)
            end_y1 = self.length_of_arm * math.sin(angle)

        # Apply rotation to the arm
            rotated_end_x = end_x1 * math.cos(self.speed) - end_y1 * math.sin(self.speed)
            rotated_end_y = end_x1 * math.sin(self.speed) + end_y1 * math.cos(self.speed)

        # Add the coordinates of the center of the carousel
            end_x = self.x + rotated_end_x
            end_y = self.y + rotated_end_y

        # Display the coordinates
            label = self.font.render(f'({end_x:.1f}, {end_y:.1f})', True, WHITE)
            window.blit(label, (end_x, end_y))
    def draw(self, screen):
        # Vẽ chân đu quay
        middle_points = []
        for i in [-1, 1]:
            angle = math.pi / 2 + i * math.pi / 8
            end_x = self.x + self.base_arm_length * math.cos(angle)
            end_y = self.y + self.base_arm_length * math.sin(angle)
            draw_line(screen, hong1, (self.x, self.y), (end_x, end_y), int(self.base_arm_width))  
            middle_x = self.x + (self.base_arm_length / 2) * math.cos(angle)
            middle_y = self.y + (self.base_arm_length / 2) * math.sin(angle)
            middle_points.append((middle_x, middle_y))
        

        # Vẽ thanh ngang nối giữa hai chân đu quay
        draw_line(screen, hong1, middle_points[0], middle_points[1], self.base_arm_width_2)  # Thanh ngang

        # Vẽ đường tròn trên cánh đu quay
        draw_circle(screen, hong2, (self.x, self.y), self.circle_radius, 2)
        draw_circle(screen, hong3, (self.x, self.y), self.circle_radius_2, 2)
        draw_circle(screen, hong2, (self.x, self.y), self.circle_radius_3, 2) 

        # Vẽ cánh đu quay và tam giác
        for i in range(self.num_of_arms):
            angle = i * 2 * math.pi / self.num_of_arms + self.speed
            end_x1 = self.length_of_arm * math.cos(angle)  # Không cộng thêm self.x, đã tính trong phép quay
            end_y1 = self.length_of_arm * math.sin(angle)  # Không cộng thêm self.y, đã tính trong phép quay

            # Áp dụng phép quay cho cánh đu quay
            rotated_end_x = end_x1 * math.cos(self.speed) - end_y1 * math.sin(self.speed)
            rotated_end_y = end_x1 * math.sin(self.speed) + end_y1 * math.cos(self.speed)

            # Cộng lại để tọa độ đúng so với tâm đu quay
            end_x = self.x + rotated_end_x
            end_y = self.y + rotated_end_y

            # Vẽ cánh đu quay
            draw_line(screen, tim, (self.x, self.y), (end_x, end_y),1.5)

            # Áp dụng phép quay cho tam giác trên đường tròn
            spike_end_x = (self.circle_radius + self.spike_length) * math.cos(angle + self.speed)
            spike_end_y = (self.circle_radius + self.spike_length) * math.sin(angle + self.speed)

            # Cộng lại để tọa độ đúng so với tâm đu quay
            spike_end_x += self.x
            spike_end_y += self.y

            inner_point_1_x = self.circle_radius * math.cos(angle - math.pi / 16 + self.speed)
            inner_point_1_y = self.circle_radius * math.sin(angle - math.pi / 16 + self.speed)

            # Cộng lại để tọa độ đúng so với tâm đu quay
            inner_point_1_x += self.x
            inner_point_1_y += self.y

            inner_point_2_x = self.circle_radius * math.cos(angle + math.pi / 16 + self.speed)
            inner_point_2_y = self.circle_radius * math.sin(angle + math.pi / 16 + self.speed)

            # Cộng lại để tọa độ đúng so với tâm đu quay
            inner_point_2_x += self.x
            inner_point_2_y += self.y

            draw_polygon(screen, hong4, [(spike_end_x, spike_end_y), (inner_point_1_x, inner_point_1_y), (inner_point_2_x, inner_point_2_y)])

            # Chọn màu ngẫu nhiên cho chỗ ngồi ở đầu cánh
            seat_color = selected_colors[i % num_of_seats]

            # Vẽ chỗ ngồi ở đầu cánh
            seat_x = end_x - self.seat_width / 2
            seat_y = end_y
            draw_rect(screen, seat_color, (seat_x, seat_y, self.seat_width, self.seat_height),5)

            # Vẽ nút kết nối giữa cánh và chỗ ngồi
            draw_circle(screen, hong3, (int(end_x), int(end_y)), self.connection_radius)

        # Vẽ trung tâm của đu quay
        draw_circle(screen, hong2, (self.x, self.y), self.center_radius)
    def update(self):
        if self.animation_running:
            self.speed += 0.008

