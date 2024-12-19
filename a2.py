import turtle #importing libaray
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)

pen=turtle.Turtle()

for i in range(1,5):
    pen.forward(100)
    pen.right(90)

turtle.done()