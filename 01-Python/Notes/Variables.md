# Variables in Python

## What is a Variable?
A variable is a container used to store data.

Example:
name = "Akshaay"

## Rules
- Must start with a letter or _
- Cannot start with a number
- Case-sensitive

## Naming Convention
student_name
employee_salary

## Multiple Assignment
a, b = 10, 20

## Dynamic Typing
x = 10
x = "Python"    

## Ways of running python file:
1. Run a python code via IDLE (Python shell)
2. Run python code via cmd
3. Run python code via notepad/notepad ++(save file with .py) and give that location in cmd

## IDE used is Pycharm or VS code 

## Keywords reserved in Python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 
'yield']

## Data types
1. Text type: str
2. Numeric types: int, float
3. Sequence types: list, tuple
3. Mapping types: dict
4. Set types: set
5. Boolean type: bool (True/False)

## Variables 
Name = AK ----> 'Name' is variable which store value 'AK'
1. A variable is nothing but a reserved memory location to store values
2. Variables are used to store the data
3. Memory allocated when the values are stored in variables
4. Every variable must have some type
5. Python is dynamically typed programming language

Q1. What are global variables?

Answer: Variables declared outside a class or function and accessible throughout the program.

Q2. What are class variables?

Answer: Variables declared inside a class but outside methods, shared by all objects of the class.

Q3. What are local variables?

Answer: Variables declared inside a function or method that are accessible only within that function.

Q4. Why do we use self.a instead of a?

Answer: self refers to the current object, allowing access to its class or instance variables.