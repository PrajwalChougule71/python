# Defualt argument
# def average(a=9, b=1):
#     print("The Average is: ",(a+b)/2)
    
# average(b=48)

# second program

# def name(fname, mname, lname):
#     print("Hello", fname, mname, lname)
    
# name("Prajwal", "Shantinath", "Chougule")

# average of multiple numbers

# def average(*numbers):
#     sum = 0 
#     for i in numbers:
#         sum = sum + i
#     print("The Avrage is: ", sum/ len(numbers))
    
# average(5,5,5)

# return statment

def average(*numbers):
    sum = 0 
    for i in numbers:
        sum = sum + i
    return sum/ len(numbers)
c = average(5,2,3,4)
print(c)