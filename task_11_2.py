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
turtle.shape('turtle')
turtle.tracer(0,0)

def duga_small():
    for i in range(0,50,2):
        turtle.forward(0.1)
        turtle.left(7.2)

duga_small()


turtle.done()