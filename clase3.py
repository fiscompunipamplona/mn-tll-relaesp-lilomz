import math as mt

#cambio de coordenadas

r=float( input("ingrese el valor de r="))
a=float( input("ingrse el valor del angulo en grados ="))

b=a*mt.pi/180

x=r*mt.cos(b)
y=r*mt.sin(b)

print(x,y)

#ejercicio nave

d=float(input( "ingrese la distancia en años luz de la tierra al planeta ")) #ly
v=float(input( "ingrese la velocidad de la nave como una fraccion de c ")) #m/s

X=d*9.5e15 #m
j=1/(mt.sqrt(1-(v**2)))
c=3e8 #m/s
T=X/v #tiempo visto desde la tierra
N=j*(T-(v*X/c)) #tiempo desde la nave

print(T,N)


#secuencia de Fibonacci

f1=1
f2=1
f3=f1+f2
x = 0

while 0<1000:
	f1=f2
	f2=f3
	f3=f1+f2
	x += 1

print(f3) #imprime la iteracion 1000


