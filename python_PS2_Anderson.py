# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:35:52 2019

@author: rayde
"""
import numpy as np 

#w=1/[l*(I-A*(1+r))^(-1)*y]

#what was given in initial problem
Iron	= np.array([90,50,40,200,180])
Coal	= np.array([120	,125,40	,500,	285])
Wheat	=[60, 150, 200, 550, 410]
labor_units	=[11,19,30,60]

transaction_table = np.array([iron, coal, wheat, labor_units])

iron = [.45, .1, 0.072727273]
coal = [.6,.25, 0.072727273]
wheat = [.3, .3, 0.363636364]

matrix_A = np.array([iron, coal, wheat])
vector_I = np.array([.055,.038,0.054545455]) 

row1 = [1,0,0] 
row2 = [0,1,0]
row3 = [0,0,1]

identity_matrix = np.array([row1, row2, row3])

matrix_IA = identity_matrix - matrix_A

#we know how to transpose a matrix
transpose = np.matrix.getH(matrix_IA) #Hermitian transpose of a matrix or use .T


a = matrix_IA[1:].T[1:].T
determ = np.linalg.det(a)

#look up adjoint matrix and define look up cofactor matrix and define
#Adjoint1 = 
Adjoint2 = Adjoint1.T #Transpose of Adjoint1 or use getH() command

#copied and pasted adjoint matrix
adjoint_of_Matrix = np.array([[0.455454545, 0.403636364, 0.405],[0.085454545, 0.328181818,0.195],[0.061818182,0.083636364,0.3525]])

#we know how to get determinants
determ_A = np.linalg.det(matrix_IA)

#Leontief inverse
inverse_IA= Adjoint2/determ_A

r = 0.10

profit_rate = (1+r)

matrix_IAU = (matrix_IA*profit_rate)

#y = 

x = [l*(z*y]

final_ans = 1/x
