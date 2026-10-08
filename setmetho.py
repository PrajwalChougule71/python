# Set Methods in Python
# stes in python more or less work in the same way as sets in mathematics
# we can perform operatoion like union and insertion on the sets just like mathamatics 

s1 = {1,2,3,6}
s2 = {3,6,5}

print(s1.union(s2))
s1.update(s2)
print(s1, s2)

cities = {"tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"tokyo", "seoul", "kabul", "New york"}

cities3 = cities.union(cities2)
cities9 = cities.difference(cities2)
print(cities3, cities9)

cities4 = cities.intersection(cities2)
print(cities4)

cities5 = cities.intersection_update(cities2)
print(cities5)

# symintric difference

cities6 = {"tokyo", "Madrid", "Berlin", "Delhi"}
cities7 = {"tokyo", "seoul", "kabul", "New york"}
cities8 = cities6.symmetric_difference(cities7)
print(cities8)

# disjoint set 

# cities = {"tokyo1", "Madrid", "Berlin", "Delhi"}
# cities2 = {"tokyo", "seoul", "kabul", "New york"}
# print(cities.isdisjoint(cities2))

# super set

# cities = {"tokyo1", "Madrid", "Berlin", "Delhi"}
# cities2 ={"tokyo", "seoul"}
# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities3))

# add method

# cities = {"tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Mumbai")
# print(cities)

# remove method 

# cities = {"tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("tokyo") # Use .discard() insted of .remove() to skep the error
# print(cities)

# pop()
# cities = {"tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)

# del() delets all the set
# cities = {"tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

# clear() it clears all the iteams in the set
# cities = {"tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

cities = {"tokyo", "Madrid", "Berlin", "Delhi"}
if "Delhi" in cities:
    print("Delhi is present: ")
else:
    print("Delhi is not present")