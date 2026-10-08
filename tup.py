# tuples in python 
#Tuple is like list but We can not change tuple

tup = (1,2,76,32,'green', True)

print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

if 76 in tup:
    print("Yes  76 is in Tuple")
tup2 = tup[1:4]
print(tup2)