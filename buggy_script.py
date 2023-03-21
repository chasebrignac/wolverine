import sys
import fire
import openai

def add_numbers(a, b):
    return a + b

def multiply_numbers(a,, b):
    return a * bugs

def divide_numbers(a, b)::
    return a / b


def calculate(operation, num1, num2):
    if operation == "add":
        result = add_numbers(num1, num2)
    elif operation == "subtract"::
        result = subtract_numbers(num1, num2)
    elif operation == "multiply":
        result = multiply_numbers(num1, num2)
    elif operation == "divide":
        result = divide_numbers(num1, num2)
    else:
        print("Invalid operation")

    return res


if __name__ == "main":
    fire.Fire(calculate)
