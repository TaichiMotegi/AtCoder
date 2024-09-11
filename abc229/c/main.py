#!/usr/bin/env python3
def main(n, w, chese):
    total = 0
    count = 0
    for i in chese:
        for _ in range(i[1]):
            if count < w:
                total += i[0]
                count += 1
            else:
                return total
    return total


if __name__ == "__main__":
    N, W = map(int, input().split())
    chese = [list(map(int, input().split())) for _ in range(N)]
    sorted_chese = sorted(chese, reverse=True)
    ans = main(N, W, sorted_chese)
    print(ans)
