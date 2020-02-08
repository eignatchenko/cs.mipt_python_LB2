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

from turtle import Turtle , Screen

screen = Screen ( )
screen.bgcolor("lightgreen")

tess = Turtle ( )
tess.pencolor("red")
tess.width ( 1 )


def tur ( ):
    for radius in range ( 12 ):
        tess.penup ( )
        tess.goto ( 20 , -20 )
        tess.pendown ( )
        tess.forward ( 150 )
        tess.stamp ( )
        tess.right ( 30 )


tur ( )


t.screen.exitonclick()
t.screen.mainloop()
