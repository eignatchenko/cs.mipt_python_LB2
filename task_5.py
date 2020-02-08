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

from turtle import Turtle, Screen

HYPOTENUSE = 0.7
#HYPOTENUSE = (2 ** 0.5) / 2


screen = Screen()
# screen.bgcolor("lightgreen")

tess = Turtle()
#tess.pencolor("red")
tess.setheading(45)
tess.width(1)

for radius in range(20, 120, 20):
    tess.penup()
    tess.goto(radius/2, -radius/2)
    tess.pendown()
    tess.circle(radius * HYPOTENUSE, steps=3)

screen.exitonclick()