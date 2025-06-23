def postfix(s):
    stk = []
    operators = set(['+', '-', '*', '/'])
    res =0
    for c in s:
        if c.isdigit():
            stk.append(int(c))
        elif c in operators:
            a = stk.pop()
            b = stk.pop()

            if c == '+':
                res = b + a
            elif c == '-':
                res = b - a
            elif c == '*':
                res = b * a
            elif c == '/':
                if a == 0:
                    return "Division by zero error"
                res = b / a
            stk.append(res)

    return stk[0]

def prefix(s):
    stk = []
    operators = set(['+', '-', '*', '/'])
    s = s[::-1]  # Reverse the string for prefix evaluation
    res = 0
    for c in s:
        if c.isdigit():
            stk.append(int(c))
        elif c in operators:
            a = stk.pop()
            b = stk.pop()

            if c == '+':
                res = a + b
            elif c == '-':
                res = a - b
            elif c == '*':
                res = a * b
            elif c == '/':
                if b == 0:
                    return "Division by zero error"
                res = a / b
            stk.append(res)

    return s[0]

def postfix_to_infix(s):
    stk = []
    operators = set(['+', '-', '*', '/'])
    for c in s:
        if c.isalnum():
            stk.append(c)
        elif c in operators:
            a = stk.pop()
            b = stk.pop()
            expression = f"({b}{c}{a})"
            stk.append(expression)
    return stk[0]

def prefix_to_infix(s):
    stk = []
    operators = set(['+', '-', '*', '/'])
    s = s[::-1]  # Reverse the string for prefix evaluation
    for c in s:
        if c.isalnum():
            stk.append(c)
        elif c in operators:
            a = stk.pop()
            b = stk.pop()
            expression = f"({a}{c}{b})"
            stk.append(expression)
    return stk[0]

def decode_to_String(s):
    stk = []

    for c in s:
        if c != ')':
            stk.append(c)
        else:
            substr = ''
            while stk and stk[-1] != '(':
                substr = stk.pop() + substr  # Reversed here naturally
            stk.pop()  # Remove '('

            num = ''
            while stk and stk[-1].isdigit():
                num = stk.pop() + num

            num = int(num) if num else 1
            stk.append(substr * num)

    return ''.join(stk)


if __name__ == "__main__":
    # Example usage
    # s = "23*54*+9-"
    # print("Postfix Evaluation:", postfix(s))
    #
    # s_prefix = "-+*2345"
    # print("Prefix Evaluation:", prefix(s_prefix))
    #
    s_infix = "23*54*+9-"
    print("Postfix to Infix:", postfix_to_infix(s_infix))
    s_prefix_infix = "-+*2345"
    print("Prefix to Infix:", prefix_to_infix(s_prefix_infix))

    s_decode = "2(a)3(bc)"
    print("Decoded String:", decode_to_String(s_decode))


