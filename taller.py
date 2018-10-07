#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import funciones as fu
class Derivada:
    def __init__(self,f,metodo="adelante",dx=0.001):
        self.f=f
        self.metodo=metodo
        self.dx=dx
        def adelante(f,x,dx):
            return fu.adelante
        def central(f,x,dx):
            return fu.central
        def extrapolada(f,x,dx):
            return fu.extrapolada
        def calc(self,x):
            if metodo =="adelante":
                c=adelante(f,x,dx)
                return c
            if metodo =="central":
                c=central(f,x,dx)
                return c
            if metodo == "extrapolada":
                c = extrapolada(f,x,dx)
                return c
            print (c)
            