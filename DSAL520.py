# def priority(x):
#     if x == '+' or x == '-':
#         return 1
#     if x == '*' or x == '/':
#         return 2
#     if x == '^':
#         return 3
#     return 0

# def infix_to_postfix(exp):
#     stack = []
#     result = ""

#     for x in exp:
#         if x.isalnum(): 
#             result += x

#         elif x == '(':
#             stack.append(x)

#         elif x == ')':
#             while stack[-1] != '(':
#                 result += stack.pop()
#             stack.pop()

#         else:
#             while stack and priority(stack[-1]) >= priority(x):
#                 result += stack.pop()
#             stack.append(x)

#     while stack:
#         result += stack.pop()

#     return result

# exp = input("Enter infix expression: ")
# print("Postfix:", infix_to_postfix(exp))



def postfix_to_infix(exp):
    stack = []

    for x in exp:
        if x.isalnum():  # Operand
            stack.append(x)
        else:  # Operator
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append("(" + op1 + x + op2 + ")")

    return stack[-1]

exp = input("Enter postfix expression: ")
print("Infix:", postfix_to_infix(exp))
