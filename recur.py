# Recurtion function in python
# Recurtion is the process of defining something in terms of it self
# In python we know that a function. It is even a possible for the function to call itself. 
# this type of construct are termed as recursive function 
 
#  factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))
print(factorial(5))


# fibonachi serise

# f(0) = 0 
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)   
# print the fibonachi sequence  
