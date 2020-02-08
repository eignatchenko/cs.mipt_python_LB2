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

from math import pi, sin, cos
from turtle import Turtle , Screen

screen = Screen ( )
t = Turtle ( )

g = 0.05

for i in range ( 500 ):
    t.forward ( g )
    t.left ( 5 )
    g += 0.05

t.screen.exitonclick ( )
t.screen.mainloop ( )
