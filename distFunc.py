import math, os
import matplotlib.pyplot as plt

def distance(x1,y1,x2,y2):
    dist=math.pow((x2-x1),2)+math.pow((y2-y1),2)
    return math.sqrt(dist)

x1=int(input("X1:\t"))
x2=int(input("X2:\t"))
y1=int(input("Y1:\t"))
y2=int(input("Y2:\t"))

print(distance(x1,y1,x2,y2))

X=[x1,x2]
Y=[y1,y2]

plt.scatter(X,Y, s=70,c='red',marker='^')

plt.title('Co-ordinates Plot On Cartesian\nDistance Between two points is: '+str(distance(x1,y1,x2,y2)))
plt.xlabel('X axis plots')
plt.ylabel('Y axis plots')

plt.show()

