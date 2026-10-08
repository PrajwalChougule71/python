#  It is a swich statment 

x = int(input("Enmter your Value of X: "))
match x:
    case 0:
        print("X is 0")
    case 4:
        print("X is 4")
    case _ if x!=90:
        print(x,"Is not 90")
    case _ if x!=80:
        print(x,"Is not 80")
    case _:
        print(x)