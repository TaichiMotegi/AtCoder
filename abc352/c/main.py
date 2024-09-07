def solution(intervals):
    result = []
    ##
    for interval in sorted(intervals):
        print(interval)
        if not result:
            result.append(interval)
        elif result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


l = [[1, 3], [0, 3], [4, 5]]

print(solution(l))
