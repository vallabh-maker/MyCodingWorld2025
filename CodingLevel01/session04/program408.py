#Program to print the chessboard using nested loops
import turtle as bot

i = 1

step = 50
angle = 90
bot.speed(100)
bot.penup()
bot.backward(step*4)
bot.left(angle)
bot.forward(step*4)
bot.right(angle)
bot.pendown()
while i <= 8:
    if i%2 == 1:
        j = 1
        while j <= 8:
            if j%2 == 1:
                s = 1
                while s <= 4:
                    bot.forward(step)
                    bot.right(angle)
                    s += 1
                bot.forward(step)
            else:
                bot.begin_fill()
                s = 1
                while s <= 4:
                    bot.forward(step)
                    bot.right(angle)
                    s += 1
                bot.forward(step)
                bot.end_fill()
            j += 1
        i += 1
        bot.backward(step*8)
        bot.right(angle)
        bot.forward(step)
        bot.left(angle)
    else:
        j = 1
        while j <= 8:
            if j%2 == 0:
                s = 1
                while s <= 4:
                    bot.forward(step)
                    bot.right(angle)
                    s += 1
                bot.forward(step)
            else:
                bot.begin_fill()
                s = 1
                while s <= 4:
                    bot.forward(step)
                    bot.right(angle)
                    s += 1
                bot.forward(step)
                bot.end_fill()
            j += 1
        i += 1
        bot.backward(step*8)
        bot.right(angle)
        bot.forward(step)
        bot.left(angle)
                
        
        
                    
            
        
        
