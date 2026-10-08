# Finally Key words in python 

def fun1():
    try:
        l = [1, 2, 6, 5]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0 
    
    finally:
        print("I am alwyas exicuted") #finally always exicuted 
        
x = fun1()
print(x)