def solution(num):
    answer = set()
    d = 2
    while d <= num:
        if num % d == 0:
            answer.add(d)
            num = int(num / d)
        else:
            d = d+1
    return answer


print(solution(600851475143))
