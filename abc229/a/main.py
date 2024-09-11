#!/usr/bin/env python3
def checkDisc(s1, s2):
    if s1 == "#." and s2 == ".#":
        return False
    elif s1 == ".#" and s2 == "#.":
        return False
    else:
        return True


if __name__ == "__main__":
    S1 = input()
    S2 = input()
    result = checkDisc(S1, S2)
    print("Yes" if result else "No")
