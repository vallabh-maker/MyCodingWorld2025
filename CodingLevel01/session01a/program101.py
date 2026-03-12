# to draw a red square with blue border

import turtle as bot
step = 100
angle = 90
bot.pencolor('blue')
bot.fillcolor('red')
bot.begin_fill()
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.end_fill()
