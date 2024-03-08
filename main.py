import pygame
import sys
import numpy as np
import du_quay
from swing import *
from background import*
from config import*
from cay import*
from nuahinhtron import*
from may import*
from xekem import*
import subprocess

pygame.init()
screen = pygame.display.set_caption("Công viên 2D")
screen = pygame.display.set_mode((screen_width + border_width, screen_height ))
control_panel = pygame.Surface((control_panel_width, control_panel_height))
control_panel.fill((100, 100, 100)) # Fill with a gray color

background = Background()
background.add_rounded_rect(x=400, y=500, width=300, height=70, stairs=5, color=(co1), radius=20)
background.add_rounded_rect(x=400, y=500, width=250, height=45, stairs=3, color=(co2), radius=10)
background.add_rounded_rect(x=430, y=525, width=180, height=15, stairs=5, color=(co1), radius=7)
background.add_rounded_rect(x=120, y=410, width=560, height=50, stairs=4, color=(co4), radius=20)
background.add_rounded_rect(x=440, y=420, width=245, height=70, stairs=5, color=(dat), radius=20)
background.add_rounded_rect(x=440, y=430, width=240, height=15, stairs=5, color=(dat2), radius=7)
background.add_circle(685, 435, 15, (troi))
background.add_rounded_rect(x=120, y=410, width=280, height=25, stairs=5, color=(co3), radius=9)
background.add_rounded_rect(x=90, y=370, width=620, height=50, stairs=4, color=(co4), radius=20)
background.add_rounded_rect(x=50, y=450, width=700, height=70, stairs=4, color=(co3), radius=30)
background.add_rounded_rect(x=50, y=480, width=500, height=40, stairs=4, color=(dat), radius=15)
background.add_circle(116, 435, 15, (troi))
background.add_circle(680, 435, 15, (troi))
#font
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 24)
text_font=pygame.font.Font(None, 18)

button_surface = pygame.Surface((button_width, button_height))
button_surface.fill((0, 255, 255)) # Fill with a blue color
button_label = button_font.render("Stop Animation", True, (0, 255, 255))
text_rect = button_label.get_rect(center=(button_width/2, button_height/2))
control_panel.blit(button_surface, (button_x1, button_y1))
label = button_font.render("3D Rectangle", True, (255, 255, 255))
text_color = (150, 0, 0) 

# Tạo bề mặt văn bản
text_surface = text_font.render("press up and down to zoom in and zoom out", True, text_color)

# Create objects
swing = Swing(screen_width / 2 - 275, 420, 70, 20, 90, 110, 15)
carousel = du_quay.Carousel(x=340, y=192, length_of_arm=126, num_of_arms=16, speed=0.015,
                            center_radius=18, base_arm_length=192, base_arm_width=5,
                            circle_radius=26, circle_radius_2=63, circle_radius_3=126,
                            spike_length=9, seat_width=15, seat_height=23,
                            connection_radius=3, base_arm_width_2=2)
# Create the first Bezier curve object with the control points
control_points_bezier1 = [(350, 370), (370, 220), (440, 200), (460, 240)]
bezier_curve1 = BezierCurve(control_points_bezier1)

# Create the second Bezier curve object with different control points
control_points_bezier2 = [(460, 240), (560,350), (600,0), (700, 370)]
bezier_curve2 = BezierCurve(control_points_bezier2)

# Chia đều diện tích các đường cong và lấy các điểm
num_points = 10  # Số điểm muốn chia
curve_points1 = bezier_curve1.calculate_evenly_spaced_points(num_points)

rows_params = [
        {'num_half_circles': 2, 'x': 430, 'y': 520, 'radius': 11, 'color': (co2)},
        {'num_half_circles': 3, 'x': 600, 'y': 520, 'radius': 10, 'color': (co2)},
        {'num_half_circles': 4, 'x': 350, 'y': 479, 'radius': 10, 'color': (co1)},
        {'num_half_circles': 2, 'x': 250, 'y': 420, 'radius': 10, 'color': (co3)},
        {'num_half_circles': 3, 'x': 600, 'y': 450, 'radius': 10, 'color': (co3)},
        {'num_half_circles': 2, 'x': 550, 'y': 420, 'radius': 10, 'color': (co2)}
    ]
# List of objects
objects = [carousel, swing]

tree1 = Tree(130, 270, 30,1.5)
tree2 = Tree(170, 300, 30,1)
tree3 = Tree(210, 276, 30,1.4)
tree4 = Tree(250, 318, 30,0.7)
tree5 = Tree(380, 300, 30,1)
tree6 = Tree(420, 270, 30,1.5)
tree7 = Tree(460, 318, 30,0.7)
tree8 = Tree(500, 300, 30,1)
tree9 = Tree(600, 318, 30,0.7)
tree10 = Tree(660, 300, 30,1)

trees = [tree1, tree2, tree3, tree4,tree5,tree6,tree7,tree8,tree9,tree10]

co = [
    circle(120, 360, 20, (co1)),
    circle(160, 360, 40, (co1)),
    circle(200, 360, 30, (co1)),
    circle(240, 360, 40, (co1)),
    circle(280, 360, 25, (co1)),
    circle(320, 360, 30, (co1)),
    circle(360, 360, 20, (co1)),
    circle(400, 360, 40, (co1)),
    circle(440, 360, 30, (co1)),
    circle(480, 360, 45, (co1)),
    circle(520, 360, 25, (co1)),
    circle(560, 360, 35, (co1)),
    circle(600, 360, 40, (co1)),
    circle(640, 360, 25, (co1)),
    circle(676, 370, 30, (co1)),
]

airplanes = [
    MayBay(x=random.randint(-50, -20) + i * 300, y=random.randint(50, 150), width=50, height=30, color=(255, 255, 255))
    for i in range(3)
]
clock = pygame.time.Clock() 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for obj in objects:
                    swing.zoom(1.1)
                    carousel.zoom(1.1)
                    obj.update()
                    obj.draw(screen)
                for airplane in airplanes:
                    airplane.zoom(1.1)
                    airplane.update()
                    airplane.draw(screen)
            elif event.key == pygame.K_DOWN:
                for obj in objects:
                    swing.zoom(0.9)
                    carousel.zoom(0.9)
                    obj.update()
                    obj.draw(screen)
                for airplane in airplanes:
                    airplane.zoom(0.9)
                    airplane.update()
                    airplane.draw(screen)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button_x2 <= mouse_pos[0] <= button_x2 + button_width2 and button_y2 <= mouse_pos[1] <= button_y2 + button_height2:
                subprocess.Popen(["pythonw", "toado3d.py"], shell=True)
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
            # The button was clicked
                if selected_object == swing:
                    for seat in swing.seats:
                        seat.speed = 0 if seat.speed != 0 else 0.05
                elif selected_object == carousel:
                    carousel.animation_running = not carousel.animation_running
                else:
                    for seat in swing.seats:
                        seat.speed = 0 if seat.speed != 0 else 0.05
                    carousel.animation_running = not carousel.animation_running
            if button_x1 <= event.pos[0] <= button_x1 + button_width and button_y1 <= event.pos[1] <= button_y1 + button_height:
                # Toggle the show_label attribute of the swing object
                if selected_object == swing:
                    swing.show_label = not swing.show_label
                elif selected_object == carousel:
                    show_coordinates = not show_coordinates
            elif swing.collidepoint(mouse_pos):
                # The swing object was clicked
                selected_object = swing
            elif carousel.collidepoint(mouse_pos):
                # The carousel object was clicked
                selected_object = carousel
    screen.fill(troi)
    for airplane in airplanes:
        airplane.update()
        airplane.draw(screen)
    # Lấy tọa độ của con chuột
    mouse_pos = pygame.mouse.get_pos()
    # Xóa vùng hiển thị tọa độ cũ
    screen.fill(WHITE, (850, 10, 140, 50))
    # Tính toán tọa độ mới của con chuột
    new_mouse_pos = (mouse_pos[0] , (mouse_pos[1] ))
    screen.blit(control_panel, (control_panel_x, control_panel_y))
    # Kiểm tra xem con chuột có nằm trong vùng tọa độ không
    if mouse_pos[0] >= 0 and mouse_pos[0] <= 800 and mouse_pos[1] >= 0 and mouse_pos[1] <= 600:
        # Vẽ tọa độ mới lên màn hình
            text = font.render(f" {new_mouse_pos}", True, BLACK)
            screen.blit(text, (850, 10))
            
    # Draw the first Bezier curve
    curve_points1 = bezier_curve1.calculate_evenly_spaced_points(num_points)
    pygame.draw.lines(screen, (sau), False, curve_points1, 2)

    # Draw the second Bezier curve
    curve_points2 = bezier_curve2.calculate_evenly_spaced_points(num_points)
    pygame.draw.lines(screen, (sau), False, curve_points2, 2)

    tree1.draw_support_columns(screen, curve_points1)
    tree2.draw_support_columns(screen, curve_points2)
    carousel.draw(screen)
    # Draw the trees
    for tree in trees:
        tree.draw(screen)
    for circle in co:
        circle.draw(screen)
    
    background.draw_background(screen)
    
    # Use the draw_half_circles_row function to draw the multiple rows of connected half-circles
    draw_half_circles_row(screen, rows_params)
    
    
    for obj in objects:
        obj.update()
        obj.draw(screen)
    button_label1 = button_font.render("Coordinates", True, (0, 255, 255))
    text_rect1 = button_label1.get_rect(center=(button_width/2, button_height/2))
    pygame.draw.rect(screen, (0, 0, 255), (button_x1, button_y1, button_width, button_height))
    pygame.draw.rect(screen, (0, 0, 255), (button_x, button_y, button_width, button_height))
    pygame.draw.rect(screen, button_color2, (button_x2, button_y2, button_width2, button_height2))
    screen.blit(button_label, (button_x + 10, button_y + 10))
    screen.blit(button_label1, (button_x1+10, button_y1 +10))
    button_surface.blit(button_label1, text_rect1)
    screen.blit(label, (button_x2 + (button_width2 - label.get_width()) / 2, button_y2+ (button_height2 - label.get_height()) / 2))
    button_surface.blit(button_label, text_rect)
    
    swing.update()
    swing.draw(screen)
    if  show_coordinates:
        carousel.show_coordinates(screen)
        airplane.show_coordinates(screen)
        
    draw_ice_cream_truck(screen, 400, 390)
    screen.blit(text_surface, (text_x, text_y))
    # Update the display
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)