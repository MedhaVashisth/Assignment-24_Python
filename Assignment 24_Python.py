#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Def : In python, def defined functions are commonly used because of their simplicity. The def defined functions do not return anything if not explicitly returned whereas the lambda function does return an object. The def functions must be declared in the namespace. The def functions can perform any python task including multiple conditions, nested conditions or loops of any level, printing, importing libraries, raising Exceptions, etc. 
Lambda : The lambda functions can be used without any declaration in the namespace. The lambda functions defined above are like single-line functions. These functions do not have parenthesis like the def defined functions but instead, take parameters after the lambda keyword as shown above. There is no return keyword defined explicitly because the lambda function does return an object by default.

2. The lambda keyword in Python provides a shortcut for declaring small anonymous functions. Lambda functions behave just like regular functions declared with the def keyword. They can be used whenever function objects are required.

3. Both map and reduce have as input the array and a function you define. They are in some way complementary: map cannot return one single element for an array of multiple elements, while reduce will always return the accumulator you eventually changed.

4. Function annotations are arbitrary python expressions that are associated with various part of functions. These expressions are evaluated at compile time and have no life in python’s runtime environment. Python does not attach any meaning to these annotations. They take life when interpreted by third party libraries, for example, mypy.

5. In programming terms, a recursive function can be defined as a routine that calls itself directly or indirectly.
Using the recursive algorithm, certain problems can be solved quite easily. Towers of Hanoi (TOH) is one such programming exercise. Try to write an iterative algorithm for TOH. Moreover, every recursive program can be written using iterative methods.
Mathematically, recursion helps to solve a few puzzles easily.
For example, a routine interview question,
get_ipython().set_next_input('In a party of N people, each person will shake her/his hand with each other person only once. In total how many hand-shakes would happen');get_ipython().run_line_magic('pinfo', 'happen')

There are three types of recursion : Head Recursion, Tail Recursion, Body Recursion

6. Coding rules and guidelines ensure that software is:

Safe: It can be used without causing harm.
Secure: It can’t be hacked.
Reliable: It functions as it should, every time.
Testable: It can be tested at the code level.
Maintainable: It can be maintained, even as your codebase grows.
Portable: It works the same in every environment.
    
7. A Function in Python is a piece of code which runs when it is referenced. It is used to utilize the code in more than one place in a program. It is also called method or procedure. Python provides many inbuilt functions like print(), input(), compile(), exec(), etc. but it also gives freedom to create your own functions.

