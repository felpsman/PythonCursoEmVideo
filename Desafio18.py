angulo=float(input())
from math import radians
rad= radians(angulo)
from math import sin
from math import cos
from math import tan
sen = sin(rad)
cosen= cos(rad)
tang = tan(rad)
print("O angulo em seno, coseno e tangente eh, respectivamente: {:.3f} {:.3f} {:.3f}".format(sen,cosen,tang))