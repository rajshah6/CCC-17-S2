n = int(input())
numbers = [int(i) for i in input().split()]
numbers.sort()

answer = []

# even
if n % 2 == 0:
    length = n//2
    lowTide = numbers[:length]
    highTide = numbers[length:]

    for i in range(length):
        answer.append(lowTide[length - 1 - i])
        answer.append(highTide[i])

#odd
else:
    lowestVal = numbers[0]
    del numbers[0]

    length = n // 2
    lowTide = numbers[:length]
    highTide = numbers[length:]

    for i in range(length):
        answer.append(lowTide[length - 1 - i])
        answer.append(highTide[i])

    answer.append(lowestVal)

answer = [str(i) for i in answer]
answer = " ".join(answer)

print(answer)
