import random
import math

def function(x, y):
	return ((1.5 - x + (x*y))**2) + ((2.25 - x + ((x*y)**2))**2) + ((2.625 - x + ((x*y)**3))**2)
	# (1.5-x +(x*y))^2 + (2.25-x+(x*y))^2 + (2.625-x+(x*y))^2
	#return (3 * ((x**2) + (y**2))) + (4*x*y) + (5*x) + (6*y) + 7

def approximations(a0, b0, Tmax, Tmin, rateCold, alfa):
	x = random.randrange(a0, b0)/10
	y = random.randrange(a0, b0)/10
	print("x, y inicial: ", x, y)
	T = Tmax
	n=0
	while T>Tmin:
		n+=1
		xNew = x+(alfa*random.gauss(0, 1))
		yNew = y+(alfa*random.gauss(0, 1))
		if (xNew<a0):
			xNew=a0
		elif (xNew>(b0/10)):
			xNew=b0/10
		if (yNew<a0):
			yNew=a0
		elif (yNew>(b0/10)):
			yNew=b0/10
		deltaE=function(xNew, yNew)-function(x, y)
		if function(x, y)>function(xNew, yNew):
			x=xNew
			y=yNew
		elif math.exp(-(abs(deltaE))/T)>random.randrange(0,10)/10:
			x=xNew
			y=yNew
		T=T*rateCold
		
	print(x, y)
	print("Evaluación", function(x, y))
	print("Iteraciones: ", n)

approximations(-20, 20, 2, 0.0001, 0.999, 0.1)


