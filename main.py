""""
This app is the simulation of a smiple calculator on python command line
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



    
