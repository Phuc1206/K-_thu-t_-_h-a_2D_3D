from graphics import *
from math import cos, sin, radians, sqrt

# Function to perform Cabinet projection
def cabinet_projection(x, y, z):
    angle = 45  # Angle for Cabinet projection (45 degrees)
    x_prime = (x - z * cos(angle)) + 250
    y_prime = (y - z * sin(angle))*(-1) + 250
    return x_prime, y_prime

def draw_line(win, x1, y1, x2, y2,max_iterations= 100):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy
    draw = True
    iterations = 0
    while iterations < max_iterations:
        if draw:
            win.plot(x1,y1)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
        iterations += 1
def draw_dashed_line(win, p1, p2, dash_length=3, max_iterations= 1000):
    x0, y0 = p1.x, p1.y
    x1, y1 = p2.x, p2.y
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    count = 0
    draw = True
    iterations = 0
    while iterations < max_iterations:
        if draw:
            win.plot(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
        count += 1
        if count == dash_length:
            count = 0
            draw = not draw

        iterations += 1

# Function to draw a 3D rectangle using Cabinet projection
def draw_3d_rectangle_cabinet(win, x, y, z, width, height, depth):
    # Calculate the projected coordinates of the rectangle
    x1, y1 = cabinet_projection(x, y, z)
    x2, y2 = cabinet_projection(x + width, y, z)
    x3, y3 = cabinet_projection(x + width, y + height, z)
    x4, y4 = cabinet_projection(x, y + height, z)

    x5, y5 = cabinet_projection(x, y, z + depth)
    x6, y6 = cabinet_projection(x + width, y, z + depth)
    x7, y7 = cabinet_projection(x + width, y + height, z + depth)
    x8, y8 = cabinet_projection(x, y + height, z + depth)

    # Draw the front face of the rectangle
    # draw_dashed_line(win, Point(x1, y1), Point(x2, y2))
    draw_dashed_line(win, Point(x2, y2), Point(x3, y3),height-3)
    draw_dashed_line(win, Point(x3, y3), Point(x4, y4),width-3)
    # draw_dashed_line(win, Point(x4, y4), Point(x1, y1))
    
    draw_line(win,x1,y1,x2,y2,width-3)
    draw_line(win,x1,y1,x4,y4,height-3)
    draw_line(win,x4,y4,x8,y8,depth-3)
    draw_line(win,x1,y1,x5,y5,depth-3)
    draw_line(win,x2,y2,x6,y6,depth-3)
    #line0 = Line(Point(x1,y1), Point(x2, y2))
    #line1 = Line(Point(x1,y1), Point(x4, y4))
    #line2 = Line(Point(x4,y4), Point(x8, y8))
    #line3 = Line(Point(x1,y1), Point(x5, y5))
    #line4 = Line(Point(x2,y2), Point(x6, y6))
    
    #line0.draw(win)
    #line1.draw(win)
    #line2.draw(win)
    #line3.draw(win)
    #line4.draw(win)
    draw_line(win,x5,y5,x6,y6,width-3)
    draw_line(win,x6,y6,x7,y7,height-3)
    draw_line(win,x7,y7,x8,y8,width-3)
    draw_line(win,x8,y8,x5,y5,height-3)
    #line5 = Line(Point(x5, y5), Point(x6, y6))
    #line6 = Line(Point(x6, y6), Point(x7, y7))
    #line7 = Line(Point(x7, y7), Point(x8, y8))
    #line8 = Line(Point(x8, y8), Point(x5, y5))
    
    #line5.draw(win)
    #line6.draw(win)
    #line7.draw(win)
    #line8.draw(win)


    # # Draw the back face of the rectangle
    # draw_dashed_line(win, Point(x5, y5), Point(x6, y6))
    # draw_dashed_line(win, Point(x6, y6), Point(x7, y7))
    # draw_dashed_line(win, Point(x7, y7), Point(x8, y8))
    # draw_dashed_line(win, Point(x8, y8), Point(x5, y5))

    # Connect the front and back faces of the rectangle
    #draw_dashed_line(win, Point(x1, y1), Point(x5, y5))
    #draw_dashed_line(win, Point(x2, y2), Point(x6, y6))
    draw_dashed_line(win, Point(x3, y3), Point(x7, y7),5,depth-3)
    # draw_dashed_line(win, Point(x4, y4), Point(x8, y8))
    
    print(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8)
    
def draw_coordinate_system(win):
    # Draw the x-axis
    line_x = Line(Point(250, 250), Point(450, 250))
    line_x.setArrow("last")
    line_x.draw(win)

    # Draw the y-axis
    line_y = Line(Point(250, 250), Point(250, 50))
    line_y.setArrow("last")
    line_y.draw(win)

    # Draw the z-axis
    line_z = Line(Point(250, 250), Point(100, 400))
    line_z.setArrow("last")
    line_z.draw(win)

    # Add labels for the axes
    label_x = Text(Point(470, 250), "x")
    label_x.draw(win)

    label_y = Text(Point(250, 30), "y")
    label_y.draw(win)

    label_z = Text(Point(90, 390), "z")
    label_z.draw(win)

def main():
    # Create the graphics window
    win = GraphWin("3D Rectangle - Cabinet Projection", 900, 600)
    draw_coordinate_system(win)
    
    #error text
    
    error_text = Text(Point(300,590),"")
    error_text.setTextColor("red")
    error_text.draw(win)
    
    #tao o nhap lieu cho ve hinh hop chu nhat
    x_rectangle_label = Text(Point(550, 70), "X:")
    x_rectangle_input = Entry(Point(610, 70), 10)
    x_rectangle_label.draw(win)
    x_rectangle_input.draw(win)

    y_rectangle_label = Text(Point(550, 100), "Y:")
    y_rectangle_input = Entry(Point(610, 100), 10)
    y_rectangle_label.draw(win)
    y_rectangle_input.draw(win)

    z_rectangle_label = Text(Point(550, 130), "Z:")
    z_rectangle_input = Entry(Point(610, 130), 10)
    z_rectangle_label.draw(win)
    z_rectangle_input.draw(win)

    width_rectangle_label = Text(Point(540, 160), "Width:")
    width_rectangle_input = Entry(Point(610, 160), 10)
    width_rectangle_label.draw(win)
    width_rectangle_input.draw(win)

    height_rectangle_label = Text(Point(535, 190), "Height:")
    height_rectangle_input = Entry(Point(610, 190), 10)
    height_rectangle_label.draw(win)
    height_rectangle_input.draw(win)
    
    depth_rectangle_label = Text(Point(540, 220), "Depth:")
    depth_rectangle_input = Entry(Point(610, 220), 10)
    depth_rectangle_label.draw(win)
    depth_rectangle_input.draw(win)
    
    # tao o nhap lieu ve hinh lap phuong
    x_cube_label = Text(Point(750, 70), "X:")
    x_cube_input = Entry(Point(820, 70), 10)
    x_cube_label.draw(win)
    x_cube_input.draw(win)

    y_cube_label = Text(Point(750, 100), "Y:")
    y_cube_input = Entry(Point(820, 100), 10)
    y_cube_label.draw(win)
    y_cube_input.draw(win)

    z_cube_label = Text(Point(750, 130), "Z:")
    z_cube_input = Entry(Point(820, 130), 10)
    z_cube_label.draw(win)
    z_cube_input.draw(win)
    
    length_cube_label = Text(Point(750, 220), "Length:")
    length_cube_input = Entry(Point(820, 220), 10)
    length_cube_label.draw(win)
    length_cube_input.draw(win)
    
    #tao nut ve
    rectangular_button = Rectangle(Point(530, 290), Point(670, 330))
    rectangular_button.setFill("white")
    rectangular_button.draw(win)
    rectangular_text = Text(Point(600, 310), "Draw Rectangular")
    rectangular_text.draw(win)

    cube_button = Rectangle(Point(750, 290), Point(870, 330))
    cube_button.setFill("white")
    cube_button.draw(win)
    cube_text = Text(Point(810, 310), "Draw Cube")
    cube_text.draw(win)
    

    # Draw the 3D rectangle using Cabinet projection
    while True:
        
        click_point = win.getMouse()
        
        if (530 < click_point.getX() < 670) and (290 < click_point.getY() < 330):
            x_text = x_rectangle_input.getText()
            y_text = y_rectangle_input.getText()
            z_text = z_rectangle_input.getText()
            width_text = width_rectangle_input.getText()
            height_text = height_rectangle_input.getText()
            depth_text = depth_rectangle_input.getText()
            if x_text and y_text and z_text and width_text and height_text and depth_text:
                x = int(x_text)
                y = int(y_text)
                z = int(z_text)
                width = int(width_text)
                height = int(height_text)
                depth = int(depth_text)
                draw_3d_rectangle_cabinet(win, x, y, z, width, height, depth)
            else:
                error_text.setText("Please enter values for both x, y, z, width, height, depth")
        elif (750 < click_point.getX() < 870) and (290 < click_point.getY() < 330):
            x_text = x_cube_input.getText()
            y_text = y_cube_input.getText()
            z_text = z_cube_input.getText()
            length_text = length_cube_input.getText()
            if x_text and y_text and z_text and length_text:
                x = int(x_text)
                y = int(y_text)
                z = int(z_text)
                length = int(length_text)
                width = height = length
                depth = length/2
                draw_3d_rectangle_cabinet(win, x,y,z,width,height,depth)
            else:
                error_text.setText("Please enter values for both x, y, z, length")
    
    # draw_3d_rectangle_cabinet(win, x, y, z, width, height, depth)

    # Wait for the user to close the window
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
