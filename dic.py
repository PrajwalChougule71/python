# Dictionary in python 
# Dictionaries are orderd collaction of dada iteams. they store multiple iteams 
# in a single variable itams are key value pair that are sepreted by commas and enclosed within curly brackets{}

dic = {
    "Prajwal": "Human being", "Spoon": "Object"
}

print(dic["Prajwal"])

info = {'name': 'PRAJWAL', 'age': 21, 'eligible': True}
print(info)
# print(info['name2']) it shows the error massage
print(info.get('name2')) #it shows a none massage
print(info.keys())
print(info.values())
print(info.items())


for key in info.keys():
    print(info[key])
    
for key in info.keys():
    print(f"the value corresponding to the key {key} is {info[key]}")