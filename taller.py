#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import funciones as fu
import numpy as np
from scipy import optimize
class Derivada:
    def __init__(self,f,metodo,dx=0.001):
        self.f=f
        self.metodo=metodo
        self.dx=dx
    def calc(self,x):
        if self.metodo =="adelante":
            c=fu.adelante(self.f,x,self.dx)
            return c
        if self.metodo =="central":
            c=fu.central(self.f,x,self.dx)
            return c
        if self.metodo == "extrapolada":
            c = fu.extrapolada(self.f,x,self.dx)
            return c
        else: return(print("los metodos son adelante, central y extrapolada"))

class Zeros:
    def __init__(self,f,metodo,error=1e-4,max_iter=100):
        self.f=f
        self.metodo=metodo
        self.error=error
        self.max_iter=max_iter
    def zero(self,vi):
        a=(vi[0])
        b=(vi[1])
        if self.metodo=="newton":
            d = fu.newton(self.f,a,self.error,self.max_iter)
            return d
        if self.metodo == "bisectriz":
            d = fu.bisectriz(self.f,a,b,self.error,self.max_iter)
            return d
        if self.metodo == "interpolacion":
            d = fu.interpolacion(self.f,a,b,self.error,self.max_iter)
            return d
        if self.metodo == "newton-sp":
            d = optimize.newton(self.f,a,tol=self.error,maxiter=self.max_iter)
            return d
        if self.metodo == "fsolve-sp":
            d = optimize.fsolve(self.f,a,xtol=self.error,maxfev=self.max_iter)
            return d
        if self.metodo == "brentq-sp":
            d = optimize.brentq(self.f,a,b,xtol=self.error,maxiter=self.max_iter)
            return d
        else: return(print ("los metodos son newton, bisectriz, interpolacion, newton-sp, fsolve-sp, brentq-sp"))

if __name__=="__main__":
    H=Derivada(np.sin,"extrapolada",0.001)
    dh=H.calc(3)
    print(dh)
    G=Zeros(np.sin,"interpolacion")
    zg=G.zero((3,3.3))
    print(zg)
else:
    pass
