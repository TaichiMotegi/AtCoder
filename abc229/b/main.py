#!/usr/bin/env python3
def main(a, b):
    flag = False
    while a != 0 and b != 0:
        if (a % 10 + b % 10) >= 10:
            flag = True
            break
        else:
            a //= 10
            b //= 10
    return flag


if __name__ == "__main__":
    A, B = map(int, input().split())
    result = main(A, B)
    print("Hard" if result else "Easy")
