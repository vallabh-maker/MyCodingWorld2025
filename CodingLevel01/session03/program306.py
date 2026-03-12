#Program to draw a square using a while loop.

import turtle as bot

step = 100
angle = 90
i = 1

while i<= 4:
    bot.forward(step)
    bot.right(angle)
    i += 1
