#  Docstrings and PEP-8

# Python docstring is a string literal that apper right after the defination, method, class, module

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) # It prints the docstring

# PEP-8
# This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. Please see the companion informational PEP describing style guidelines for the C code in the C implementation of Python.

# This document and PEP 257 (Docstring Conventions) were adapted from Guido’s original Python Style Guide essay, with some additions from Barry’s style guide [2].

# This style guide evolves over time as additional conventions are identified and past conventions are rendered obsolete by changes in the language itself.

# Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project.

# The Zen Of Python
# import this