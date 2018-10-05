#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
def adelante(f,x,dx=10000):
    return (f(x+dx)-f(x))/dx
def central(f,x,dx=10000):
    return (f(x+dx/2) - f(x-dx/2))/dx
def extrapolada(f,x,dx=10000):
    F1=(f(x+dx/2) - f(x-dx/2))/dx
    F2=(f(x+dx/4)-f(x-dx/4))/(dx/2)
    return (4*F2-F1)/3
print(adelante(np.sin,0))