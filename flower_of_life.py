import turtle as t
import math


r = 30

t.teleport(0, 0)
t.circle(r)
t.teleport(0, -30)
t.circle(2*r)

#assuming r is the hypotenuse, we can calculate adjacent and opposit 
for i in range(6):
    o = math.cos(math.radians(i*60)) * r
    a = math.sin(math.radians(i*60)) * r
    print(a,o)
    t.teleport(o, a)
    t.circle(r)



