#1) program to draw a square
import turtle as robot


step = 100
angle= 90

robot.pensize(5)

#draw red bordered square
robot.pencolor('red')
robot.forward(step)
robot.left(angle)
robot.forward(step)
robot.left(angle)
robot.forward(step)
robot.left(angle)
robot.forward(step)
robot.left(angle)

#Go to next position
robot.penup()
robot.forward(step*2)
robot.pendown()

#draw blue boredered rectangle
robot.pencolor('blue')
robot.forward(step)
robot.right(angle)
robot.forward(step*2)
robot.right(angle)
robot.forward(step)
robot.right(angle)
robot.forward(step*2)
robot.right(angle)


