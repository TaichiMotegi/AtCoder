def solution(island, trip):
    position = 0
    distance = []
    for i in trip:
        for j in range(position, len(island)):
            if i == island[j]:
                distance.append(j - position)
                position = j
                break
    return sum(distance)


solution("abcdefghijklnmopqrstuvwxyz", "hire")
