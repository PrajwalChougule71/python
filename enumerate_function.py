# Enumerate function in python

marks = [12, 25, 32, 56, 60]

# index = 0
# for marks in marks:
#     print(marks)
#     if(index == 3):
#         print("Prajwal, awesome")
#     inedx +=1


# The main code 

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Prajwal, awesome")
  
  
# Second type

# for index, mark in enumerate(marks, start=1):
#     print(mark)
#     if(index == 3):
#         print("Prajwal, awesome")
  