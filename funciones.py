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
def newton(f,a,error=1e-10,max_iter=100): #se va a hacer con la derivada central
    x2=a-(f(a)/central(f,a))
    i = 1
    while m.fabs(f(x2)-0)>error and i<max_iter:
        a=x2
        x2=a-(f(a)/central(f,a))  
        i +=1
    return (x2)
def bisectriz(f,a,b,error=1e-10,max_iter=100):
    c=(a+b)/2.0
    i=1
    while m.fabs(f(c)-0)>error and i<max_iter:
        if f(c)*f(a)<0:
            b=c
            c=(a+b)/2.0
        else:
            a=c
            c=(a+b)/2.0
        i +=1    
    return c
def interpolacion(f,a,b,error=1e-10,max_iter=100):
    c=a-(f(a)*(b-a))/(f(b)-f(a))
    i=1
    while m.fabs(f(c)-0)>error and i<max_iter:
        c=a-(f(a)*(b-a))/(f(b)-f(a))
        if f(c)*f(a)<0:
            b=c
        else:
           a=c
        i +=1    
    return c
