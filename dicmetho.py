# Dictionary method in python

ep1 = {222:33, 223:60, 224:56, 225:55}
ep2 = {226:55, 227:60}

ep1.update(ep2)
print(ep1)

ep1.clear()  #clear all the elements in dictionary
print(ep1)

empt = {}   #makes empty dictionary 
print(empt)

ep1.pop(222)  #remove the silected key and value
print(ep1)

ep1.popiteam()  #remove the last key and value
print(ep1)

# del ep1 #delets the dictionary 
# del ep1[222] #delets the selected key 