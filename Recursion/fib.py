# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    n1, n2 = 0, 1
    count = 0

    if n==1:
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1,end=' ')
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
        print()