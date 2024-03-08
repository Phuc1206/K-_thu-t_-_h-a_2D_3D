import pygame
from config import*
from shapes import *
class circle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
class Tree:
    def __init__(self, x, y, size,height_factor):
        self.x = x
        self.y = y
        self.size = size
        self.height_factor = height_factor

    def draw(self, surface):
        top_triangle_height = self.size*self.height_factor
        middle_triangle_height = self.size * self.height_factor
        bottom_triangle_height = self.size * self.height_factor *2
        # Define the points for the three triangles
        top_triangle = [(self.x, self.y-10 - top_triangle_height), (self.x - self.size, self.y), (self.x + self.size, self.y)]
        middle_triangle = [(self.x, self.y-10), (self.x - self.size, self.y + middle_triangle_height), (self.x + self.size, self.y + middle_triangle_height)]
        bottom_triangle = [(self.x, self.y-10 + middle_triangle_height), (self.x - self.size, self.y + bottom_triangle_height), (self.x + self.size, self.y + bottom_triangle_height)]

        # Draw the triangles to form the tree
        draw_filled_triangle(surface, (sau), top_triangle)  # Green triangle (top of the tree)
        draw_filled_triangle(surface, (sau), middle_triangle)  # Green triangle (middle of the tree)
        draw_filled_triangle(surface, (sau), bottom_triangle)  # Green triangle (bottom of the tree)

    def draw_support_columns(self, surface, curve_points):
        for x, y in curve_points:
            pygame.draw.line(surface, (sau), (x, y), (x, 370), 2)
class BezierCurve:
    def __init__(self, control_points):
        self.control_points = control_points

    def calculate_evenly_spaced_points(self, num_points):
        points = []
        for i in range(num_points):
            t = i / (num_points - 1)  # Tính giá trị t từ 0 đến 1 cách đều
            x = self.bezier_x(t)
            y = self.bezier_y(t)
            points.append((x, y))
        return points

    def bezier_x(self, t):
        return self.bezier(t, self.control_points[0][0], self.control_points[1][0], self.control_points[2][0], self.control_points[3][0])

    def bezier_y(self, t):
        return self.bezier(t, self.control_points[0][1], self.control_points[1][1], self.control_points[2][1], self.control_points[3][1])

    def bezier(self, t, p0, p1, p2, p3):
        return ((1 - t) ** 3) * p0 + (3 * (1 - t) ** 2 * t) * p1 + (3 * (1 - t) * t ** 2) * p2 + (t ** 3) * p3
