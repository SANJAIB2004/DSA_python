n = int(input())  # Input the number of elements for the slices
lst = list(map(int, input().split()))  # Input the list of integers

# Extract the first `n` and last `n` elements
res = lst[:n] + lst[-n:]  # Concatenate the slices

# Print the result and its type
print(res)
print(" ".join(map(str,res)))
print(type(res))  # Output the type of `res`
