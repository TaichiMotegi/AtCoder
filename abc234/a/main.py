#!/usr/bin/env python3
t = int(input())


def calc(t):
    return t**2 + 2 * t + 3


print(calc(calc(calc(t) + t) + calc(calc(t))))
