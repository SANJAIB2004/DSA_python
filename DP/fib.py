# n = 5
#
# dp = [0]*(n+1)
# dp[0] = 0
# dp[1] = 1
# print(dp[0], end=" ")
# print(dp[1], end=" ")
# for i in range(2, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
#     print(dp[i], end=" ")


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    dp = [0] * (n + 1)
    if n==0:
        return n
    elif n == 1:
        return 1
    if dp[n]!=0:
        return dp[n]
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]

n= int(input("Enter a number: "))
result = fib(n)
print(f"The {n}th Fibonacci number is: {result}")



