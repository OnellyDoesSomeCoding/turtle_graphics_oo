import turtle
import random

# Color mode is 0 to 1

class Polygons:
    def __init__(self, sides: int):
        self.sides = sides
        self.size = self.set_random_size()
        self.orientation = self.set_random_orientation()
        self.location = self.set_random_location()
        self.color = self.set_random_color()
        self.border = self.set_random_border()

    def set_random_sides(self):
        self.sides = random.randint(3, 5)
        return self.sides

    def set_random_size(self):
        self.size = random.randint(50, 150)
        return self.size

    def set_random_orientation(self):
        self.orientation = random.randint(0, 90)
        return self.orientation

    def set_random_location(self):
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        return self.location

    def set_random_color(self):
        self.color = (random.random(), random.random(), random.random())
        return self.color

    def set_random_border(self):
        self.border = random.randint(1, 10)
        return self.border

    def randomize_all(self):
        self.set_random_size()
        self.set_random_orientation()
        self.set_random_location()
        self.set_random_color()
        self.set_random_border()

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border)
        turtle.pendown()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360/self.sides)
        turtle.penup()


while True:
    choice = int(input("Create an Abstract Art Piece (1-9): "))
    if choice == 1:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(20, 25)):
            pol = Polygons(3)
            pol.randomize_all()
            pol.draw_polygon()
        break
    elif choice == 2:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(15, 25)):
            pol = Polygons(4)
            pol.randomize_all()
            pol.draw_polygon()
        break
    elif choice == 3:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(15, 25)):
            pol = Polygons(5)
            pol.randomize_all()
            pol.draw_polygon()
        break
    elif choice == 4:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(15, 25)):
            pol = Polygons(random.randint(3, 5))
            pol.randomize_all()
            pol.draw_polygon()
        break
    elif choice == 5:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(15, 25)):
            pol = Polygons(3)
            pol.randomize_all()
            for j in range(3):
                pol.draw_polygon()
                pol.size *= 0.618
                pol.location[0] = turtle.pos()[0] + pol.size/12
                pol.location[1] = turtle.pos()[1] + pol.size/12
        break
    elif choice == 6:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(15, 25)):
            pol = Polygons(4)
            pol.randomize_all()
            for j in range(3):
                pol.draw_polygon()
                pol.size *= 0.618
                pol.location[0] = turtle.pos()[0] + pol.size/12
                pol.location[1] = turtle.pos()[1] + pol.size/12
        break
    elif choice == 7:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(15, 25)):
            pol = Polygons(5)
            pol.randomize_all()
            for j in range(3):
                pol.draw_polygon()
                pol.size *= 0.618
                pol.location[0] = turtle.pos()[0] + pol.size/5
                pol.location[1] = turtle.pos()[1] + pol.size/5
        break
    elif choice == 8:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(15, 25)):
            pol = Polygons(random.randint(3, 5))
            pol.randomize_all()
            for j in range(3):
                pol.draw_polygon()
                pol.size *= 0.618
                pol.location[0] = turtle.pos()[0] + pol.size/5
                pol.location[1] = turtle.pos()[1] + pol.size/5
        break
    elif choice == 9:
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(10, 15)):
            pol = Polygons(random.randint(3, 5))
            pol.randomize_all()
            for j in range(3):
                pol.draw_polygon()
                pol.size *= 0.618
                pol.location[0] = turtle.pos()[0] + pol.size/5
                pol.location[1] = turtle.pos()[1] + pol.size/5
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        for i in range(0, random.randint(10, 15)):
            pol = Polygons(random.randint(3, 5))
            pol.randomize_all()
            pol.draw_polygon()
        break
    else:
        print("Please select a valid option!")

turtle.done()
