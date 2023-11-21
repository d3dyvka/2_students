from tkinter import Tk, Canvas
from grid import Grid
from human import Human
import random

root = Tk()
canvas = Canvas (root, width = 800, height=600)
canvas.pack()
grid = Grid (canvas)
grid.display()
group = "ИП-22"
f = open("god.txt", 'r', encoding='utf-8')
random_people = []

for i in f:
    g = i.split(";")
    id = int(g[0])
    name = g[1]
    number = g[2]
    gender = g[4]
    random_people.append({"id":id, 'full_name':name, 'gender':gender, 'number':number})

human1 = random.choice(random_people)
name = f"{human1['full_name'].split()[0]}. {human1['full_name'].split()[1][0]}. {human1['full_name'].split()[2][0]}, {group}, №{human1['number']}"
p1 = Human(canvas, name,100,500, human1['gender'])
p1.display()

human2 = random.choice(random_people)
name = f"{human2['full_name'].split()[0]}. {human2['full_name'].split()[1][0]}. {human2['full_name'].split()[2][0]}, {group}, №{human2['number']}"
p2 = Human(canvas, name, 500, 500, human2['gender'])
p2.display()

root.mainloop()