def solution(numbers):
    total = 0
    count = 0
    answer = 0
    for n in numbers :
        total += n
        count += 1
    answer = total / count
    return answer
