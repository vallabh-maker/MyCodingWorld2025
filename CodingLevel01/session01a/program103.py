# to draw the first 2 sqaures of a chessboard

import turtle as bot

step = 50
angle = 90
bot.speed(100)
#Go to beginning position
bot.penup()
bot.backward(step*4)
bot.left(angle)
bot.forward(step*4)
bot.right(angle)
bot.pendown()
#Draw white square 1
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 1
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 2
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 2
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 3
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 3
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 4
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 4
bot.begin_fill()
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.end_fill()

#Go to the next row
bot.penup()
bot.backward(step*8)
bot.right(angle)
bot.forward(step)
bot.left(angle)

#Draw black square 5
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 5
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 6
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 6
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 7
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 7
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 8
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 8
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)

#Go to the next row
bot.backward(step*8)
bot.right(angle)
bot.forward(step)
bot.left(angle)#Draw white square 1
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 1
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 2
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 2
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 3
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 3
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 4
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 4
bot.begin_fill()
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.end_fill()

#Go to the next row
bot.penup()
bot.backward(step*8)
bot.right(angle)
bot.forward(step)
bot.left(angle)

#Draw black square 5
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 5
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 6
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 6
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 7
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 7
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 8
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 8
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)

#Go to the next row
bot.backward(step*8)
bot.right(angle)
bot.forward(step)
bot.left(angle)#Draw white square 1
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 1
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 2
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 2
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 3
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 3
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 4
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 4
bot.begin_fill()
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.end_fill()

#Go to the next row
bot.penup()
bot.backward(step*8)
bot.right(angle)
bot.forward(step)
bot.left(angle)

#Draw black square 5
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 5
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 6
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 6
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 7
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 7
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 8
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 8
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)

#Go to the next row
bot.backward(step*8)
bot.right(angle)
bot.forward(step)
bot.left(angle)#Draw white square 1
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 1
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 2
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 2
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 3
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 3
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 4
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 4
bot.begin_fill()
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.end_fill()

#Go to the next row
bot.penup()
bot.backward(step*8)
bot.right(angle)
bot.forward(step)
bot.left(angle)

#Draw black square 5
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 5
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black square 6
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white sqaure 6
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 7
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 7
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw black sqaure 8
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

#Go to next position
bot.penup()
bot.forward(step)
bot.pendown()

#Draw white square 8
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)
bot.right(angle)
bot.forward(step)

#Go to the next row
bot.backward(step*8)
bot.right(angle)
bot.forward(step)
bot.left(angle)




