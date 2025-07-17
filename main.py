""""
This app is the simulation of a smiple calculator on python command line that reads infix, prefix, and postfi expressions.
It supports addition, subtraction, multiplication, division, and exponentiation.
It also handles errors such as division by zero and invalid expressions.
It is designed to be used in a command line interface and can be extended with more features.
It is a simple calculator that can be used for basic arithmetic operations.
"""
import math


def add(x, y):
    """Add two numbers."""
    return x + y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x /y

def subtract(x, y): 
    """Subtract two numbers."""
    return x - y   

def exponentiate(x, y):
    """Raise x to the power of y."""
    return x ** y

def evaluate_infix(expression):
    """Evaluate a mathematical expression."""
    new_expression = expression.replace(" ", "")
    precedence = lambda op: 1 if op in "+-" else 2 if op in "*/" else 3 if op == '^' else 0
    apply_operator = lambda op, left, right: (add(left, right) if op == '+' else
                                              subtract(left, right) if op == '-' else
                                              multiply(left, right) if op == '*' else
                                              divide(left, right) if op == '/' else
                                              exponentiate(left, right))
    operands = []
    i = 0
    while i < len(new_expression):
        if new_expression[i].isdigit():
            num = 0
            while i < len(new_expression) and new_expression[i].isdigit():
                num = num * 10 + int(new_expression[i])
                i += 1
            operands.append(num)
        elif new_expression[i] in "+-*/^":
            while (operators and operators[-1] in "+-*/^" and
                   precedence(operators[-1]) >= precedence(new_expression[i])):
                right = operands.pop()
                left = operands.pop()
                op = operators.pop()
                operands.append(apply_operator(op, left, right))
            operators.append(new_expression[i])
            i += 1
        else:
            raise ValueError(f"Invalid character: {new_expression[i]}")
    
    while operators:
        right = operands.pop()
        left = operands.pop()
        op = operators.pop()
        operands.append(apply_operator(op, left, right))
    
    return operands[0]

def prefix_evaluator(expression):
    """Evaluate a prefix expression."""
    stack = []
    tokens = expression.split()[::-1]
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in "+-*/^":
            if len(stack) < 2:
                raise ValueError("Insufficient values in the expression.")  
            left = stack.pop()
            right = stack.pop() 
            if token == '+':
                stack.append(add(left, right))
            elif token == '-':
                stack.append(subtract(left, right))
            elif token == '*':
                stack.append(multiply(left, right))
            elif token == '/':
                stack.append(divide(left, right))
            elif token == '^':
                stack.append(exponentiate(left, right))
        else: 
            raise ValueError(f"Invalid token: {token}")
    if len(stack) != 1:
        raise ValueError("The expression is invalid.")
    return stack[0]


    

