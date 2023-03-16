from math import pi


def circle(r):
    return pi*r**2


def square(s):
    return s**2


def rectangle(s, l):
    return s*l


def triangle(h, s):
    return .5*s*h


def get_func(li):
    return [eval(i.strip()) for i in li]

