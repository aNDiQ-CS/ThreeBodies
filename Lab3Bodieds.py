from tkinter import *
from math import atan, sin, cos, pi, sqrt

G = 6.67 * pow(10, -11)


class Planet:
    def __init__(self, x, y, color, mass):
        self.coords = [x, y]
        self.size = (20, 20)
        self.movementVector = [0, 0]
        self.mass = mass * pow(10, 24)
        self.color = color
        self.ball = c.create_oval(self.coords[0] - self.size[0] / 2, self.coords[1] - self.size[0] / 2,
                                  self.coords[0] + self.size[0] / 2, self.coords[1] + self.size[1] / 2,
                                  fill=self.color)

    def move(self, x, y):
        self.coords[0] += x
        self.coords[1] += y
        c.move(self.ball, x, y)
        c.create_oval(self.coords[0] - 0.5, self.coords[1] - 0.5,
                      self.coords[0] + 0.5, self.coords[1] + 0.5,
                      fill=self.color)

    def do_force(self, planets):
        for p in planets:
            delta = pow(10, 11)
            vector = [p.coords[0] - self.coords[0], p.coords[1] - self.coords[1]]
            if vector[0] == 0:
                alpha = pi
            elif vector[0] < 0:
                alpha = atan(vector[1] / vector[0]) + pi
            else:
                alpha = atan(vector[1] / vector[0])
            vector_length = sqrt(pow(vector[0], 2) + pow(vector[1], 2))
            if vector_length < self.size[0]:
                vector_length = self.size[0]
            F = G * self.mass * p.mass / pow(vector_length, 2)

            if vector[0] == 0:
                Fx = 0
            else:
                Fx = F * cos(alpha)

            if vector[1] == 0:
                Fy = 0
            else:
                Fy = F * sin(alpha)

            self.movementVector[0] += Fx / self.mass / delta
            self.movementVector[1] += Fy / self.mass / delta


root = Tk()
c = Canvas(root, width=800, height=800, bg="#AAAAAA")
c.pack()
p0 = Planet(400, 400, "red", 1)
p1 = Planet(420, 200, "green", 1)
p2 = Planet(200, 550, "blue", 1)
# p3 = Planet(400, 700, "Yellow", 1)
# p4 = Planet(100, 100, "Pink", 1)
# p5 = Planet(200, 200, "Black", 1)
planet_list = [p0, p1, p2]

time = 1
while True:
    root.update()
    for i in range(len(planet_list)):
        current_planets = planet_list.copy()
        current_planets.pop(i)
        #planet_list[i].do_force(current_planets)
        root.after(time, planet_list[i].do_force(current_planets))
    for p in planet_list:
        p.move(p.movementVector[0], p.movementVector[1])

root.mainloop()
