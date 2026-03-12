#Program to code chess board with a loop

import turtle as t

step = 50
angle = 90
i = 1

t.penup()
t.backward(step*4)
t.left(angle)
t.forward(step*4)
t.right(angle)
t.pendown()
t.speed(0)
r = 1
while i <= 64:
        if i%2 == 1 and i <= 8:
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.right(angle)  
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.right(angle)
            t.forward(step)
            i += 1
        elif i%2 == 0 and i <= 8:
            t.begin_fill()
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.right(angle)  
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.end_fill()
            i += 1
        if i == 9:
            t.backward(step*8)
            t.right(angle)
            t.forward(step)
            t.left(angle)
        if i%2 == 1 and i > 8:
            t.begin_fill()
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.right(angle)  
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.end_fill()
            i += 1
        elif i%2 == 0 and i > 8:
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.right(angle)  
            t.forward(step)
            t.right(angle)
            t.forward(step)
            t.right(angle)
            t.forward(step)
            i += 1
        if i > 16:
            t.backward(step*8)
            t.right(angle)
            t.forward(step)
            t.left(angle)
            i = 1
            r += 1
        if r == 5:
            i = 65
        
    
            


