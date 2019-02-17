# Draw cycle out of 
import turtle

def draw_square(a_turtle):
  for i in range(1,5):
    print("{0} time".format(i))
    a_turtle.forward(100)
    a_turtle.right(90)

def draw_art():
  window = turtle.Screen()
  window.bgcolor("green")

  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.speed(2)

  for i in range(1, 37):
    print("{0} time".format(i))
    draw_square(brad)
    brad.right(10)

  window.exitonclick()

draw_art()