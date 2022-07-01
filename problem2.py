def fibo(n):
    if n <= 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = 1
while fibo(num) < 4000000:
    num = num + 1
print(num)

answer = 0
for n in range(1, 34):
    if fibo(n) % 2 == 0:
        answer = answer + fibo(n)
print(answer)
