from math import ceil, modf, fmod

def to_nearest_cent(number):

	x = number * 100
	return (ceil(x) if modf(x)[0] >= 0.5 else floor(x)) * 0.01

def to_nearest_even_cent(number):

	x = number * 100
	x = modf(x)[1]
	return x * 0.01 if fmod(x, 2) == 0 else (x + 1) * 0.01

#Идею округления подсмотрел у @nimcrash т.к не нашел более оптимального решения