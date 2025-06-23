def odd_occurrence_string(s):
    seen = set()
    result = ""
    for ch in s:
        if ch in seen:
            seen.remove(ch)
        else:
            seen.add(ch)
            result += ch
    return result

# Example
input_str = "i have got gold"
print(odd_occurrence_string(input_str))
