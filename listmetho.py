# list methods in python

l = [1,5,2,3,4,8,0]
print(l)
l.append(7) #adds the numbers in last position in the list
l.sort() # Short the list 
l.reverse() #Revears the sting 
l.sort(reverse=True) #It reverse the stirng
print(l.index(1)) # It prints the index in that position
print(l.count(3)) #It counts the given variables in list
print(l)
l.insert(1, 500) # it inserts the 500 in list in position of 1

# m = l
# m[0] = 0
# print(l)

m = [100, 200, 300]
l.extend(m)
print(l) # It add m list in l list

#  There is another method to add
k = l + m
print(k)