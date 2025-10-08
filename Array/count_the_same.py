def count_same_bits(a, b):
    xor_val = a ^ b
    diff_bits = bin(xor_val).count('1')
    print(diff_bits)
    same_bits = 32 - diff_bits
    return same_bits

def binary_pair_similarity(input1, input2):
    result = []
    for num in input1:
        total = 0
        for i in range(num):
            total += count_same_bits(i, i+1)
        result.append(total)
    return result

# Example
input1 = list(map(int,input().split()))
input2 = int(input())
output = binary_pair_similarity(input1, input2)
print(output)
