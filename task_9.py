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
pen = turtle.Turtle()
pen.speed(1)
pen.up()
pen.setposition(-30,30)
pen.down()
def rightMNOG(n,dlina):
    sumAngle = (n-2)*180
    angle = sumAngle/n
    for i in range(n):
        pen.left ( 180 - angle )
        pen.forward(dlina)

for i in range(3,11):
    rightMNOG(i,50)

turtle.done()