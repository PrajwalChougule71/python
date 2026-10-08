# Importe module in python

# from math import * (It imports all functions in math module)
import math

result = math.sqrt(9)
print(result)

# Second option 

# from math import sqrt, pi

# result = sqrt(9)
# print(result)

# The other type

# import math (import math as m)

# result = math.sqrt(9) (We can write it as m.sqrt)
# print(result)

# from math import sqrt as s

# result = s(9)
# print(result)

# We can see all math module function using this 

# import math
# print(dir(math))
# print(math.nan, type(math.nan))

from main import welcome, Prajwal

welcome()
print(Prajwal)