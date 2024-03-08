import pygame
from math import cos, sin, pi
from config import*
from shapes import*


def draw_gear(screen, x, y, num_teeth, inner_radius, outer_radius, color, thickness):
    for i in range(num_teeth):
        angle = 2 * pi * i / num_teeth
        x1 = x + int(inner_radius * cos(angle))
        y1 = y + int(inner_radius * sin(angle))
        x2 = x + int(outer_radius * cos(angle))
        y2 = y + int(outer_radius * sin(angle))
        draw_line(screen, color, (x1, y1), (x2, y2), thickness)

    # Vẽ các đoạn thẳng liên kết các răng của bánh răng
    for i in range(num_teeth):
        angle = 2 * pi * i / num_teeth
        x1 = x + int(inner_radius * cos(angle))
        y1 = y + int(inner_radius * sin(angle))
        x2 = x + int(outer_radius * cos(angle))
        y2 = y + int(outer_radius * sin(angle))
        draw_line(screen, color, (x1, y1), (x2, y2), thickness)
def draw_ice_cream_truck(screen, x, y):
    
    draw_filled_rect(screen, (125,96,89), (x+70, y-30, 3, 45))
    draw_filled_circle(screen,(x+40,y-28),13,(125,96,89))
    draw_filled_circle(screen,(x+40,y-24),10,(da))
    draw_filled_rect(screen, (cam), (x+30, y-13, 20, 35))
    draw_filled_rect(screen, (vang), (x+25, y-13, 5, 35))
    draw_filled_rect(screen, (vang), (x+50, y-13, 20, 5))
    draw_filled_oval(screen, x+73, y-83, 10, 15, vang2, 0)
    draw_filled_oval(screen, x+80, y-68, 10, 15, hong5, 20)
    draw_filled_oval(screen, x+65, y-73, 10, 15, (24,143,137), -20)
    draw_filled_oval(screen, x+73, y-60, 10, 15, xanhla2, 0)
    draw_filled_oval(screen, x+80, y-40, 10, 15, vang2, 20)
    draw_filled_oval(screen, x+65, y-45, 10, 15, hong5, -20)    
    draw_filled_rect(screen, (da2), (x, y, 100, 55))
    draw_filled_rect(screen, (xanh1), (x + 5, y, 10, 55))
    draw_filled_rect(screen, (xanh1), (x + 25, y, 10, 55))
    draw_filled_rect(screen, (xanh1), (x + 45, y, 10, 55))
    draw_filled_rect(screen, (xanh1), (x + 65, y, 10, 55))
    draw_filled_rect(screen, (xanh1), (x + 85, y, 10, 55))
    draw_filled_rect(screen, (125,96,89), (x+8, y+55, 6, 12))
    draw_filled_rect(screen, (hong2), (x-3, y, 106, 8))
    draw_filled_rect(screen, (hong2), (x-3, y + 55, 106, 4))   
    draw_circle(screen,(125,96,89), (x+93, y+50), 22,5)
    draw_gear(screen, x + 93, y + 50, 7, 0, 22, (125, 96, 89), 2)