#Program to define a function to accept side of a sqaure and draw a sqaure

def draw_sqaure(side):
    k = 1
    while k <= 4:
        bot.forward(side)
        bot.right(90)
        k += 1
        
def draw_coloured_sqaure(side, color):
    k = 1
    bot.fillcolor(color)
    bot.begin_fill()
    while k <= 4:
        bot.forward(side)
        bot.right(90)
        k += 1
    bot.end_fill()

    
import turtle
bot = turtle.Turtle()

draw_coloured_sqaure(100, 'red')



    
