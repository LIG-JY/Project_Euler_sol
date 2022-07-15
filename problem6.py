def sigmasquare(k,n):
    result = 0
    for num in range(k, n+1):
        result += num**2
    return result


def totalsumsquare(k,n):
    result = 0
    for num in range(k, n+1):
        result += num
    return result**2


def solution(k,n):
    return totalsumsquare(k,n) - sigmasquare(k,n)


print(solution(1,100))
