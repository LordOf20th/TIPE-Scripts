# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:14:22 2020

@author: Charlotte PÉTÉ, Louis LACOSTE, Louis MAILLET
"""
from matplotlib import pyplot as plt

def graph2mesures(M1,M2):
    if len(M1) == len(M2):
        X = []
        for i in range(2*len(M1)):
            X.append(i//2+1)
        Y = []
        for i in range(len(M1)):
            Y.append(M1[i])
            Y.append(M2[i])
        return X, Y
    else:
        raise ValueError


def afficher(M):
    for i in range(0, len(M[0]), 2):
        plt.plot(M[0][i:i+2], M[1][i:i+2], 'rx-')
    plt.show()
