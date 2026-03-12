#Program to code a turtle race
'''
Steps
1. Draw the playground

2. Display the title

3. Display START and draw start line

4. Display FINISH and draw finish line

5. Create a list of 8 players and place them before the start line

6. Start the race

7. Make all the turtle move towards finish line using random module

8. Check if the turtles reach the finish.

9. Display the winner
'''

import turtle
import random
bot = turtle.Turtle()
x = 300
y = 250
bot.pensize(5)
#Step 1
bot.penup()
bot.goto(-x,-y)
bot.pendown()
bot.forward(2*x)
bot.left(90)
bot.forward(2*y)
bot.left(90)
bot.forward(2*x)
bot.left(90)
bot.forward(2*y)
bot.left(90)

#Step 2
bot.penup()
bot.goto(0,y)
bot.pendown()
bot.write("Turtle Race", align = "center", font = ('Calibri', 20 , 'bold'))

#Step 3
bot.penup()
bot.goto(-x+100,y-50)
bot.write('START', align = 'center', font = ('Arial', 15 , 'bold'))
bot.pendown()
bot.right(90)
bot.forward(y*2 - 100)

#Step 4
bot.penup()
bot.goto(x-100,y-50)
bot.pendown()
bot.write('FINISH', align = 'center', font = ('Arial', 15 , 'bold'))
bot.pendown()
bot.forward(y*2 - 100)

#Step 5
player1 = turtle.Turtle('turtle')
player2 = turtle.Turtle('turtle')
player3 = turtle.Turtle('turtle')
player1.pencolor('red')
player2.pencolor('blue')
player3.pencolor('yellow')
player1.pensize(3)
player2.pensize(3)
player3.pensize(3)
player1.penup()
player2.penup()
player3.penup()
player1.goto(-x+100,y-100)
player2.goto(-x+100,0)
player3.goto(-x+100,-y+100)
player1.pendown()
player2.pendown()
player3.pendown()
player1.write('Player 1', align = 'right')
player2.write('Player 2', align = 'right')
player3.write('Player 3', align = 'right')
player1.penup()
player2.penup()
player3.penup()

#Step 6
winner = ""
while True:
    player1.forward(random.randint(1,4))
    player2.forward(random.randint(1,4))
    player3.forward(random.randint(1,4))

    if player1.xcor() >= x-100:
        player1.right(180)
    elif player2.xcor() >= x-100:
        player2.right(180)
    elif player3.xcor() >= x-100:
        player3.right(180)

    if player1.xcor() <= -x+99:
        winner = "Player 1"
        break
    elif player2.xcor() <= -x+99:
        winner = "Player 2"
        break
    elif player3.xcor() <= -x+99:
        winner = "Player 3"
        break
        
bot.penup()
bot.goto(0,0)
msg = "The winner is" + winner
bot.pendown()
bot.write(msg, align = "center", font = ("Arial", 20, "normal"))


    
