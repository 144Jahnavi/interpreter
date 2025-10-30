import math


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []
    num = ""

    for ch in expression:
        if ch.isdigit():
            num += ch
        else:
            if num:
                output.append(num)
                num = ""
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence(ch) <= precedence(stack[-1]):
                    output.append(stack.pop())
                stack.append(ch)

    if num:
        output.append(num)

    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(arr):
    st = []
    for i in arr:
        if i.isdigit():
            st.append(int(i))
        else:
            a = st.pop()
            b = st.pop()
            if i == '+':
                st.append(b + a)
            elif i == '-':
                st.append(b - a)
            elif i == '*':
                st.append(b * a)
            elif i == '/':
                st.append(b / a)
            elif i == '^':
                st.append(b ** a)
    return st.pop()


expr = input("Enter expression: ")  
postfix_expr = infix_to_postfix(expr)
print("Result:", evaluate_postfix(postfix_expr))
