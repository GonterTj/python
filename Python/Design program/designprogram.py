import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
d = random.randint(1, 100)

from turtle import *
def r(x,y):
    rt(x)
    fd(y)

tracer(2)
fd(100)
bgcolor('black')
color('cyan')
width(3)

for i in range(2003):
    fd(i)
    r(a,i)
    r(b,i)
    r(c,i)
    r(d,i)
    circle(100,90)

done()