# to draw a blue rectangle with a red border

import turtle as bot
step1 = 200
step2 = 100
angle = 90
bot.pencolor('red')
bot.fillcolor('blue')
bot.begin_fill()
bot.forward(step1)
bot.right(angle)
bot.forward(step2)
bot.right(angle)
bot.forward(step1)
bot.right(angle)
bot.forward(step2)
bot.right(angle)
bot.end_fill()
