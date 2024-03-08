import pygame
import math
from graphics import *

def draw_line(screen, color, start_pos, end_pos, width=10):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    dx = end_x - start_x
    dy = end_y - start_y
    steps = max(abs(dx), abs(dy))

    # Calculate the slope and angle based on the line's direction
    if dx == 0:
        angle = math.pi / 2  # 90 degrees
    else:
        angle = math.atan(dy / dx)

    d = width // 2  # Half the width

    if steps == 0:
        for sign in [-1, 1]:
            offset_x = d * math.sin(angle) * sign
            offset_y = d * math.cos(angle) * sign
            new_x, new_y = start_x + offset_x, start_y - offset_y
            screen.set_at((int(round(new_x)), int(round(new_y))), color)
        return

    x_increment = dx / steps
    y_increment = dy / steps
    x, y = start_x, start_y

    for _ in range(int(steps) + 1):
        # Draw the main point
        screen.set_at((int(round(x)), int(round(y))), color)

        # Draw the points that make the line thicker
        for sign in [-1, 1]:
            offset_x = d * math.sin(angle) * sign
            offset_y = d * math.cos(angle) * sign
            new_x, new_y = x + offset_x, y - offset_y
            
            # Fill the line with color
            if sign == -1:
                prev_new_x, prev_new_y = new_x, new_y
            else:
                min_x, max_x = sorted([new_x, prev_new_x])
                min_y, max_y = sorted([new_y, prev_new_y])
                for fill_x in range(int(min_x), int(max_x)+1):
                    for fill_y in range(int(min_y), int(max_y)+1):
                        screen.set_at((fill_x, fill_y), color)
            
        x += x_increment
        y += y_increment

        
def draw_circle_filled(screen, color, center, radius):
    x0, y0 = center
    for r in range(0, int(radius + 1)):
        x = r
        y = 0
        decision = 1 - x

        while y <= x:
            screen.set_at((x + x0, y + y0), color)
            screen.set_at((y + x0, x + y0), color)
            screen.set_at((-x + x0, y + y0), color)
            screen.set_at((-y + x0, x + y0), color)
            screen.set_at((-x + x0, -y + y0), color)
            screen.set_at((-y + x0, -x + y0), color)
            screen.set_at((x + x0, -y + y0), color)
            screen.set_at((y + x0, -x + y0), color)

            for i in range(-x, x):
                screen.set_at((i + x0, y + y0), color)
                screen.set_at((i + x0, -y + y0), color)

            for i in range(-y, y):
                screen.set_at((i + x0, x + y0), color)
                screen.set_at((i + x0, -x + y0), color)

            y += 1
            if decision <= 0:
                decision += 2 * y + 1
            else:
                x -= 1
                decision += 2 * (y - x) + 1
def draw_circle(screen, color, center, radius, thickness=1):
    x0, y0 = center
    for r in range(int(radius - thickness + 1), int(radius + 1)):
        x = r
        y = 0
        decision = 1 - x

        while y <= x:
            screen.set_at((x + x0, y + y0), color)
            screen.set_at((y + x0, x + y0), color)
            screen.set_at((-x + x0, y + y0), color)
            screen.set_at((-y + x0, x + y0), color)
            screen.set_at((-x + x0, -y + y0), color)
            screen.set_at((-y + x0, -x + y0), color)
            screen.set_at((x + x0, -y + y0), color)
            screen.set_at((y + x0, -x + y0), color)

            y += 1
            if decision <= 0:
                decision += 2 * y + 1
            else:
                x -= 1
                decision += 2 * (y - x) + 1
def draw_ellipse_filled(screen, color, rect):
    x0, y0, width, height = rect
    hh = height * height
    ww = width * width
    hhww = hh * ww
    x0 += width // 2
    y0 += height // 2
    x1 = width // 2
    dx = 0

    # Draw the horizontal diameter
    for x in range(int(-x1), int(x1 + 1)):
        screen.set_at((int(x + x0), int(y0)), color)

    # Draw both halves at the same time, away from the diameter
    for y in range(1, height // 2 + 1):
        x1 = x1 - (dx - 1)  # Try slopes of dx - 1 or more
        for _ in range(int(x1)):  # If this line is shorter than the previous one
            if x1 * x1 * hh + y * y * ww <= hhww:
                break
        dx = x1 - x1  # Current approximation of the slope
        x1 = x1

        for x in range(int(-x1), int(x1 + 1)):
            screen.set_at((int(x + x0), int(y + y0)), color)
            screen.set_at((int(x + x0), int(-y + y0)), color)

def draw_filled_oval(screen, xc, yc, a, b, color, rotation_angle=0):
    
    angle_rad = math.radians(rotation_angle)
    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)

    x = 0
    y = b
    a_sqr = a * a
    b_sqr = b * b
    two_a_sqr = 2 * a_sqr
    two_b_sqr = 2 * b_sqr
    four_a_sqr = 4 * a_sqr
    four_b_sqr = 4 * b_sqr
    p = round(b_sqr - a_sqr * b + 0.25 * a_sqr)

    while two_a_sqr * y >= two_b_sqr * x:
        rotated_x = int(x * cos_angle - y * sin_angle)
        rotated_y = int(x * sin_angle + y * cos_angle)

        screen.set_at((xc + rotated_x, yc + rotated_y), color)
        screen.set_at((xc - rotated_x, yc + rotated_y), color)
        screen.set_at((xc + rotated_x, yc - rotated_y), color)
        screen.set_at((xc - rotated_x, yc - rotated_y), color)

        x += 1
        if p < 0:
            p += two_b_sqr * (2 * x + 1)
        else:
            y -= 1
            p += two_b_sqr * (2 * x + 1) - four_a_sqr * y

    p = round(b_sqr * (x + 0.5) * (x + 0.5) + a_sqr * (y - 1) * (y - 1) - a_sqr * b_sqr)

    while y >= 0:
        rotated_x = int(x * cos_angle - y * sin_angle)
        rotated_y = int(x * sin_angle + y * cos_angle)

        screen.set_at((xc + rotated_x, yc + rotated_y), color)
        screen.set_at((xc - rotated_x, yc + rotated_y), color)
        screen.set_at((xc + rotated_x, yc - rotated_y), color)
        screen.set_at((xc - rotated_x, yc - rotated_y), color)

        y -= 1
        if p > 0:
            p += two_a_sqr * (1 - 2 * y)
        else:
            x += 1
            p += two_a_sqr * (1 - 2 * y) + four_b_sqr * x
    for y in range(-b, b+1):
        for x in range(-a, a+1):
            if (x/a)**2 + (y/b)**2 <= 1:
                rotated_x = int(x * cos_angle - y * sin_angle)
                rotated_y = int(x * sin_angle + y * cos_angle)

                screen.set_at((xc + rotated_x, yc + rotated_y), color)
def draw_rect(screen, color, rect, width=1):
    x, y, w, h = rect
    start_pos = (x, y)
    end_pos = (x + w, y)
    draw_line(screen, color, start_pos, end_pos, width)

    start_pos = end_pos
    end_pos = (x + w, y + h)
    draw_line(screen, color, start_pos, end_pos, width)

    start_pos = end_pos
    end_pos = (x, y + h)
    draw_line(screen, color, start_pos, end_pos, width)

    start_pos = end_pos
    end_pos = (x, y)
    draw_line(screen, color, start_pos, end_pos, width)
def draw_polygon(screen, color, vertices, width=1):
    n = len(vertices)
    for i in range(n):
        start_pos = vertices[i]
        end_pos = vertices[(i + 1) % n]
        draw_line(screen, color, start_pos, end_pos, width)
def draw_filled_polygon(screen, color, vertices):
    n = len(vertices)
    if n < 3:
        return

    # Find the bounding box of the polygon
    min_x = min(vertices, key=lambda p: p[0])[0]
    max_x = max(vertices, key=lambda p: p[0])[0]
    min_y = min(vertices, key=lambda p: p[1])[1]
    max_y = max(vertices, key=lambda p: p[1])[1]

    # Iterate over each row of the bounding box
    for y in range(int(min_y), int(max_y) + 1):
        # Find the intersections of the row with the polygon edges
        intersections = []
        for i in range(n):
            start_pos = vertices[i]
            end_pos = vertices[(i + 1) % n]
            if start_pos[1] == end_pos[1]:
                continue
            if start_pos[1] > end_pos[1]:
                start_pos, end_pos = end_pos, start_pos
            if y < start_pos[1] or y > end_pos[1]:
                continue
            x = start_pos[0] + (y - start_pos[1]) * (end_pos[0] - start_pos[0]) / (end_pos[1] - start_pos[1])
            intersections.append(x)
        intersections.sort()

        # Check if the number of intersections is even
        if len(intersections) % 2 == 1:
            continue

        # Fill the pixels between each pair of intersections
        for i in range(0, len(intersections), 2):
            x_start = int(intersections[i])
            x_end = int(intersections[i + 1])
            for x in range(x_start, x_end + 1):
                screen.set_at((x, y), color)
def draw_filled_triangle(screen, color, vertices):
    if len(vertices) != 3:
        return

    # Find the bounding box of the triangle
    min_x = min(vertices, key=lambda p: p[0])[0]
    max_x = max(vertices, key=lambda p: p[0])[0]
    min_y = min(vertices, key=lambda p: p[1])[1]
    max_y = max(vertices, key=lambda p: p[1])[1]

    # Iterate over each row of the bounding box
    for y in range(int(min_y), int(max_y) + 1):
        # Find the intersections of the row with the triangle edges
        intersections = []
        for i in range(3):
            start_pos = vertices[i]
            end_pos = vertices[(i + 1) % 3]
            if start_pos[1] == end_pos[1]:
                continue
            if start_pos[1] > end_pos[1]:
                start_pos, end_pos = end_pos, start_pos
            if y < start_pos[1] or y > end_pos[1]:
                continue
            x = start_pos[0] + (y - start_pos[1]) * (end_pos[0] - start_pos[0]) / (end_pos[1] - start_pos[1])
            intersections.append(x)
        intersections.sort()

        # Fill the pixels between each pair of intersections
        for i in range(0, len(intersections), 2):
            x_start = int(intersections[i])
            x_end = int(intersections[i + 1])
            for x in range(x_start, x_end + 1):
                screen.set_at((x, y), color)
def draw_filled_circle(screen, center, radius, color):
    center_x, center_y = center
    x = 0
    y = radius
    d = 3 - 2 * radius

    while x <= y:
        for i in range(center_x - x, center_x + x + 1):
            screen.set_at((i, center_y + y), color)
            screen.set_at((i, center_y - y), color)
        for i in range(center_x - y, center_x + y + 1):
            screen.set_at((i, center_y + x), color)
            screen.set_at((i, center_y - x), color)

        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1

        x += 1
def draw_filled_rect(screen, color, rect, width=1):
    x, y, w, h = map(int, rect)  
    for i in range(x, x + w):
        for j in range(y, y + h):
            screen.set_at((i, j), color)