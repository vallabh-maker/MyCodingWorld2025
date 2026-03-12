#Define a function to draw a chessboard
import turtle
bot = turtle.Turtle()
bot.speed(0)
step = 50
angle = 90
bot.penup()
bot.backward(step*4)
bot.left(angle)
bot.forward(step*4)
bot.right(angle)
bot.pendown()
def draw_white_square():
    s = 1
    while s <= 4:
        bot.forward(step)
        bot.right(angle)
        s +=1
def draw_black_square():
    s = 1
    bot.fillcolor('black')
    bot.begin_fill()
    while s<= 4:
        bot.forward(step)
        bot.right(angle)
        s += 1
    bot.end_fill()
def goto_next_position():
    bot.forward(step)
def draw_row_start_white():
    n = 1
    while n <= 4:
        draw_white_square()
        goto_next_position()
        draw_black_square()
        goto_next_position()
        n += 1
def goto_next_row():
    bot.backward(step*8)
    bot.right(angle)
    bot.forward(step)
    bot.left(angle)
def draw_row_start_black():
    n = 1
    while n <= 4:
        draw_black_square()
        goto_next_position()
        draw_white_square()
        goto_next_position()
        n += 1
def draw_chessboard():
    r = 1
    while r <= 4:
        draw_row_start_white()
        goto_next_row()
        draw_row_start_black()
        goto_next_row()
        r += 1
draw_chessboard()

