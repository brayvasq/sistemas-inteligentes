"""
 * Linear regression in Javascript
 * (c) 2016, Antonio Villamarin
 * License GPL
 *
"""
import math

xarray = [1, 2, 3, 4, 5]
yarray = [5, 5, 5, 6.8, 9]
x = y = xy = xx = a = b = resultado = 0
cantidad = len(xarray)
futuro = 100;
      
for i in range(0,cantidad):
      print('Dado ' + str(xarray[i]) + ' => ' + str(yarray[i]))
      x += xarray[i]
      y += yarray[i]
      xy += xarray[i]*yarray[i]
      xx += xarray[i]*xarray[i]

b = ((cantidad * xy) - (x * y)) / ((cantidad * xx) - (x * x))

a = (y - (b * x)) / cantidad

if(b != 0):
    print('Dado ' + str(futuro) + ' => ' + str(round(a + (b * futuro))))
else:
    print('Dado ' + str(futuro) + ' => Infinito');