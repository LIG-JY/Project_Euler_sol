def checkpalindrome(target):
    if len(target) <= 1:
        return True
    else:
        if target[0] == target[-1]:
            return checkpalindrome(target[1:-1])
        else:
            return False


def solution():
    answer = set()
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if checkpalindrome(str(i*j)):
                answer.add(i*j)
    return answer

print(solution())


def mergesort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        return merge(mergesort(left), mergesort(right))


def merge(left, right):
    things = []
    leftidx, rightidx = 0 , 0
    while leftidx < len(left) and rightidx < len(right):
        if left[leftidx] > right[rightidx]:
            things.append(left[leftidx])
            leftidx = leftidx + 1
        else:
            things.append(right[rightidx])
            rightidx = rightidx + 1
    if rightidx < len(right):
        things = things + right[rightidx:]
    else:
        things = things + left[leftidx:]
    return things


answer = list(solution())
print(mergesort(answer))
