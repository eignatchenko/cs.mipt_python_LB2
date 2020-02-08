#!/usr/bin/python3

_methods = """
доступные методы:
forward(X)	Пройти вперёд X пикселей
backward(X)	Пройти назад X пикселей
left(X)	Повернуться налево на X градусов
right(X)	Повернуться направо на X градусов
penup()	Не оставлять след при движении
pendown()	Оставлять след при движении
shape(X)	Изменить значок черепахи (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
stamp()	Нарисовать копию черепахи в текущем месте
color()	Установить цвет
begin_fill()	Необходимо вызвать перед рисованием фигуры, которую надо закрасить
end_fill()	Вызвать после окончания рисования фигуры
width()	Установить толщину линии
goto(x, y)	Переместить черепашку в точку (x, y)
"""

import turtle
from math import pi
t = turtle.Pen()
t.left(90)
t.speed(1)

def big_pol():
    for x in range(180):
        t.forward(1)
        t.right(1)

def left_l():
    g = 0.05
    for i in range ( 50 ) :
        t.forward ( g/2 * pi )
        t.right ( 5 )
        g += 0.05

for i in range (4):
    big_pol()
    left_l()

t.screen.exitonclick()
t.screen.mainloop()