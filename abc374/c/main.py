#!/usr/bin/env python3
def minimax_partition(numbers):
    def dfs(index, sum1, sum2):
        if index == len(numbers):
            return max(sum1, sum2)

        option1 = dfs(index + 1, sum1 + numbers[index], sum2)

        option2 = dfs(index + 1, sum1, sum2 + numbers[index])

        return min(option1, option2)

    return dfs(0, 0, 0)


n = int(input())
numbers = list(map(int, input().split()))

result = minimax_partition(numbers)
print(result)
