import random
import math

def function(x, y):
	return (1.5-x +(x*y))*(1.5-x +(x*y)) + (2.25-x+(x*y))*(2.25-x+(x*y)) + (2.625-x+(x*y))*(2.625-x+(x*y))

def approximations(a0, b0, Tmax, Tmin, rateCold, alfa):
	x = random.randrange(a0, b0)/10
	y = random.randrange(a0, b0)/10
	print("X, Y inicial: ", x, y)
	T = Tmax
	n=0
	while T>Tmin:
		n+=1
		xNew = x+(alfa*random.gauss(0, 1))
		yNew = y+(alfa*random.gauss(0, 1))
		deltaE=function(xNew, yNew)-function(x, y)
		if function(x, y)>function(xNew, yNew):
			x=xNew
			y=yNew
		elif math.exp(deltaE/T)>random.randrange(0,1):
			x=xNew
			y=yNew
		T=T*rateCold
		if (x<a0/10):
			x=a0/10
		elif (x>(b0/10)):
			x=b0/10
		if (y<a0/10):
			y=a0/10
		elif (y>(b0/10)):
			y=b0/10
	print(x, y)
	print("Iteraciones: ", n)
			

approximations(-20, 20, 2, 0.001, 0.9, 0.01)

