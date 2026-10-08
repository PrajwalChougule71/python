# Exception handling in python 

a = input("Enter your number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e: # here e is error
    print(e)
    
print("Some imp lines of code")
print("End of program")
                
    
    
# a = input("Enter your number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e: # here e is error
#     print("Sorry some error ocurred")
    
# print("Some imp lines of code")
# print("End of program")
                   
                   
# a = input("Enter your number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except : # We dont need write Exception as e if we dont use e
#     print("Sorry some error ocurred")
    
# print("Some imp lines of code")
# print("End of program")


# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
# except ValueError:
#     print("Number is enterd is not an integer ")
# except IndexError:
#     print("Index Error")
    