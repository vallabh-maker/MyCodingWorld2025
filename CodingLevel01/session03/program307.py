#Program to prompt and accept the number of sides of a polygon and draw a polygon with those many sides.

import turtle as bot

step = 35
n = int(input("Input the number of sides of the polygon "))
angle = 360/n
i = 1
s = 1
while i <= 72:
    while s <= n:
        bot.forward(step)
        bot.right(angle)
    bot.right(5)
    i += 1
    
