# Function to process the strings
def process_strings(strings):
    result = ""
    max_len = max(len(s) for s in strings)  # Find the longest string

    # Iterate from rightmost character to leftmost
    for i in range(1, max_len + 1):
        for s in strings:
            if len(s) >= i:  # Check if string has this character from right
                result += s[-i]
    return result


# Main program
n = int(input().strip())
strings = [input().strip() for _ in range(n)]

print(process_strings(strings))
