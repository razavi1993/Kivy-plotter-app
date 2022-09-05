import numpy as np 
from sympy import *
from sympy import MutableDenseNDimArray, lambdify

x,y =symbols('x y')
z = symbols('z', real=False)

def plot_values(func_str, a, b, N):
	xs = np.linspace(a, b, N)
	ys = lambdify(x, sympify(func_str), 'numpy')(xs)
	return xs, ys

def plot_values3d(func_str, a, b, c, d, N):
	xs, ys = np.meshgrid(np.linspace(a, b, N), np.linspace(c, d, N))
	zs = lambdify([x, y], sympify(func_str), 'numpy')(xs, ys)
	return xs, ys, zs

def lambdified_func(func_str):
	return np.vectorize(lambdify(z, sympify(func_str), 'mpmath'), otypes=[complex])

def get_list(text, n):
	num_list = text.split(',')
	if len(num_list) == n:
		return num_list
	else:
		return []


