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
    operators = []
    i = 0
    while i < len(new_expression):
        if new_expression[i].isdigit():
            num = 0
            while i < len(new_expression) and new_expression[i].isdigit():
                num = num * 10 + int(new_expression[i])
                i += 1
            operands.append(num)
        elif new_expression[i] in "+-*/^":
            if new_expression[i] == '-' and (i == 0 or new_expression[i-1] in "+-*/^("):
                # Handle unary minus
                num = 0
                i += 1
                while i < len(new_expression) and new_expression[i].isdigit():
                    num = num * 10 + int(new_expression[i])
                    i += 1
                operands.append(-num)
                continue
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

def postfix_evaluator(expression):
    """Evaluates a postfix expression"""
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in "+-*/":
            if len(stack) < 2:
                raise ValueError("Insufficient values in the expression.")
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(add(left, right))
            elif token == "-":
                stack.append(subtract(left, right))
            elif token == "*":          
                stack.append(multiply(left, right))
            elif token == "/":
                stack.append(divide(left, right))
            elif token == "^":
                stack.append(exponentiate(left, right))
        else:
            raise ValueError(f"Invalid token: {token}")
    if len(stack) != 1:
        raise ValueError("The expression is invalid.")
    return stack[0]


def determine_expression_type(expression):
    """Determine the type of the expression."""
    if expression.startswith('+') or expression.startswith('-') or expression.startswith('*') or expression.startswith('/') or expression.startswith('^'):
        return 'prefix'
    elif expression.endswith('+') or expression.endswith('-') or expression.endswith('*') or expression.endswith('/') or expression.endswith('^'):
        return 'postfix'
    else:
        return 'infix'

def main():
    """Demo of the calculator."""
    print ("Welcome to the Calculator!")
    print("You can enter mathematical expressions in infix, prefix, or postfix notation. Note that negative numbers are only supported in infix notation.")
    while True:
        expression = input("Enter a mathematical expression whether infix, prefix, or postfix(enter 'exit' to quit): ")
        if expression.lower() == "exit":
            print("Exiting the app. Have a good day!")
            break
        expression_type = determine_expression_type(expression)
        try:
            if expression_type == "infix":
                result = evaluate_infix(expression)
            elif expression_type == "prefix":
                result = prefix_evaluator(expression)
            elif expression_type == "postfix":
                result = postfix_evaluator(expression)
            else:            raise ValueError("Unknown expression type.")
        
            print(f"The result is: {result}")

        except Error as e:
            print(f"Error: Oops! Are you sure you entered the right input?? {e}")
            continue
        
def create_gui_from_main():
    """Create a GUI with color and calculator looks, with buttons for each operation and numbers."""
    import tkinter as tk
    from tkinter import messagebox

    class CalculatorApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Calculator")
            self.expression = ""
            self.create_widgets()

        def create_widgets(self):
            self.display = tk.Entry(self.root, width=25, font=('Arial', 20), bd=5, relief=tk.RIDGE, justify='right')
            self.display.grid(row=0, column=0, columnspan=4, pady=10)

            buttons = [
                ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
                ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
                ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
                ('0', 4, 0), ('.', 4, 1), ('^', 4, 2), ('+', 4, 3),
                ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('=', 5, 3)
            ]

            for (text, row, col) in buttons:
                action = lambda x=text: self.on_button_click(x)
                tk.Button(self.root, text=text, width=5, height=2, font=('Arial', 16), command=action)\
                    .grid(row=row, column=col, padx=2, pady=2)

        def on_button_click(self, char):
            if char == 'C':
                self.expression = ""
                self.display.delete(0, tk.END)
            elif char == '=':
                try:
                    result = evaluate_infix(self.expression)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                    self.expression = str(result)
                except Exception as e:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Error")
                    self.expression = ""
            else:
                self.expression += str(char)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)

    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    create_gui_from_main()
else:
    print("This module is not meant to be run directly. Please import it in your main application.")
    # Ensure all tests pass before running the main function
    from test_main import test_evaluate_infix, test_prefix_evaluator, test_postfix_evaluator, test_determine_expression_type
    test_evaluate_infix()
    test_prefix_evaluator()
    test_postfix_evaluator()
    test_determine_expression_type()
    print("All tests completed successfully!")  




