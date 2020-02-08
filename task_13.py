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
t = Turtle ( )



def eyes ( radius ) :
    t.circle ( radius )


def nose ( line , gradus , nosecolor="black" ):
    t.goto ( 0 , line*2 )
    t.color ( nosecolor )
    t.begin_fill ( )
    t.pendown ( )
    t.left ( gradus )
    t.forward ( line )
    t.color ( nosecolor )
    t.end_fill ( )

def big_pol(x, y , nosecolor="black"):
    t.penup ( )
    t.goto ( x , y )
    t.color ( nosecolor )
    t.begin_fill ( )
    t.pendown ( )
    for x in range(180):
        t.backward(1)
        t.left(1)

def smile (radius1, radius2, side1, side2, outlinecol="#0000ff",fillcol="yellow" ):
    t.color ( fillcol )
    t.begin_fill ( )
    t.circle (radius2)
    t.color ( fillcol )
    t.end_fill ( )
    t.penup ( )

    for i in range (2):
        t.goto(side1,side2)
        t.color (outlinecol)
        t.begin_fill ( )
        eyes (radius1 )
        t.color ( outlinecol )
        t.end_fill ( )
        side1 = side1 * (-1)

t.reset()
t.width(5)
t.speed(5)
smile(15, 100, -40, 130)
nose (40,90)
big_pol (-60,90)

t.screen.exitonclick()
t.screen.mainloop()