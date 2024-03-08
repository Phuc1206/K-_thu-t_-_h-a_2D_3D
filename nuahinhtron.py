import pygame
import math
from shapes import *
def draw_half_circles_row(surface, rows_params):
    num_points = 100
    start_angle = 0
    end_angle = 180

    for row_params in rows_params:
        x = row_params['x']  # Starting x-coordinate for the row
        y = row_params['y']  # Y-coordinate (height) of the centers of the half-circles
        radius = row_params['radius']  # Radius of the half-circles
        spacing = 2 * radius  # Space between the centers of adjacent half-circles
        color = row_params['color']  # Color of the half-circles

        num_half_circles = row_params['num_half_circles']  # Number of half-circles in the row

        for i in range(num_half_circles):
            cx = x + i * spacing  # Calculate the x-coordinate of the center of the current half-circle

            # Store the points of the half-circle in a list
            points = []

            for i in range(num_points):
                angle = math.radians(start_angle + i * (end_angle - start_angle) / num_points)
                x1 = cx + int(radius * math.cos(angle))
                y1 = y - int(radius * math.sin(angle))  # Flip the y-coordinate to make it face upwards
                points.append((x1, y1))

            # Draw lines between the points to create the half-circle
            #pygame.draw.lines(surface, color, False, points, 2)

            # Fill the half-circle
            draw_polygon(surface, color, points,9)
