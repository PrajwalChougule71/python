# String slicing in python

# name = "prajwal"
# print(len(name))

fruit = "Mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4])
print(fruit[1:4])
print(fruit[0:-3]) #python take it always as a print(fruit[0:len(fruit)-3])




# def is_palindrome(text):
#     # Convert to lowercase for uniform comparison
#     text = text.upper()
#     # Compare string to its reverse slice
#     return text == text[::-1]

# # Examples
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("Level"))    # True
# print(is_palindrome("python"))   # False
