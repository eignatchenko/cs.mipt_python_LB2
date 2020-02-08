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
Zero = turtle.Turtle()
One = turtle.Turtle()
Two = turtle.Turtle()
Three = turtle.Turtle()
Four = turtle.Turtle()
Five = turtle.Turtle()
Six = turtle.Turtle()
Seven = turtle.Turtle()
#Eight = turtle.Turtle()

for i in  (Zero,One,Two,Three,Four,Five,Six,Seven):
    i.penup()

Zero.goto(0,50)
One.goto(0,-50)
Two.goto(-50,0)
Three.goto(50,0)
Four.goto(25,25)
Five.goto(-25,25)
Six.goto(-25,-25)
Seven.goto(25,-25)
#Eight.goto(25,25)

for i in  (Zero,One,Two,Three,Four,Five,Six,Seven):
    i.pendown ()
    i.pensize (2)

for i in  (Zero,One,Two,Three,Four,Five,Six,Seven):
    i.circle(50)



turtle.done()