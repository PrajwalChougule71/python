# Operations in tupels
# tuples are immutable if you want to add, remove or change the 
# element in tiple items then you must convert the tuple to the list
# then perform oprations on list and convert it back to list

cont = ('spin', 'india', 'italy', 'england', 'germany')
temp = list(cont)  # It converts tuple into list
temp.append('russia') # It adds the russia in the list
temp.pop(3)  # pop Used for remove the the value in list
temp[2] = 'finland'
cont = tuple(temp)
print(cont)

# addition of tuple 

cont1 = ('pak', 'afg', 'ban', 'sri')
cont2 = ('vie', 'ind', 'china')
southeastasia = cont1+cont2
print(southeastasia)

# index in tuple

tuple1 = (0,1,2,3,1,3,1,2,3)
res = tuple1.count(3)
res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('count of 3 in tuple1 is: ',res)

