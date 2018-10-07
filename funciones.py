#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math as m
def adelante(f,x,dx=1e-8):
    return (f(x+dx)-f(x))/dx
def central(f,x,dx=1e-8):
    return (f(x+dx/2) - f(x-dx/2))/dx
def extrapolada(f,x,dx=1e-8):
    F1=(f(x+dx/2) - f(x-dx/2))/dx
    F2=(f(x+dx/4)-f(x-dx/4))/(dx/2)
    return (4*F2-F1)/3
def segunda(f,x,dx=1e-8):
    return (f(x+dx)+f(x-dx)-2*f(x))/(dx**2)
def newton(f,x1,error=1e-10): #se va a hacer con la derivada central
    x2=x1-(f(x1)/central(f,x1))
    while m.fabs(f(x2)-0)>error:
        x1=x2
        x2=x1-(f(x1)/central(f,x1))        
    return (x2)
def bisectriz(f,a,b,error=1e-10):
    c=(a+b)/2.0
    while m.fabs(f(c)-0)>error:
        if f(c)*f(a)<0:
            b=c
            c=(a+b)/2.0
        else:
            a=c
            c=(a+b)/2.0
    return c
def interpolacion(f,a,b,error=1e-10):
    FX=f(a) +((f(b)-f(a))/(b-a)) *(x-a)
    