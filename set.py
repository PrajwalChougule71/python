# Sets in python
# Sets are unordered collaction of data items. srets items are sepreted by commas and enckosed with curly brtacets{}.
# Sets are unchangeble, mmeaning you can not change items of sets once created.
# sets do not containt dupliicate items. 

s = {2,3,6}
print(s)

info = {"Prajwal", 19, False, 5.9, 19}
print(info)

harry = set() # The way to print Empty set  
print(type(harry))

for value in info:
    print(value)