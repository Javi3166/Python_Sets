#Sets: unordered, mutable, no duplicates

mySet = {1, 2, 3}
print(mySet)

print("\nIf there are duplicates, it won't save them into the set.")
mySet = {1, 2, 3, 2, 1}
print(mySet)

print("\nYou can create a set using the set() function with an iterable, like a list.")
mySet = set([1, 2, 3])
print(mySet)

print("\nIt is also possible to use a string with the set() function, however it won't be saved in the same order.")
mySet = set("1, 2, 3")
print(mySet)
mySet = set("Hello!")
print(mySet)

print("\nIf I want to create an empty set, it will need to be done with set(), since just using brackets will "
      "make it a dictionary.")
mySet = {}
print(type(mySet))
mySet = set()
print(type(mySet))

print("\nIt is possible to add elements to a set with .add().")
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)
print(mySet)

print("\nIt is possible to remove elements in a set with .remove(). However, it will throw an error if the element "
      "does not exist in the set.")
mySet.remove(4)
print(mySet)
try:
    mySet.remove(5)
except KeyError:
    print("Key error encountered.")

print("\nIt is also possible to remove elements in a set using .discard() and unlike .remove(), will not throw"
      "an error if trying to discard a value not in the set.")
mySet.discard(3)
print(mySet)
mySet.discard(5)
print(mySet)

print("\nIt is possible to clear a set using .clear().")
mySet.clear()

mySet = {1, 2, 3}

print("\nIt is possible to remove the first element using the .pop() function and have it displayed too with print().")
print(mySet.pop())
print(mySet)

print("\nIt is possible to iterate over a set.")
for index in mySet:
    print(index)

print("\nIt is possible to see if an element is in a set using if ... in ...")
if 3 in mySet:
    print("It is in the set.")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {1, 2, 3 ,5, 7}

print("\nA union will combine elements from two different sets using the .union() function.")
union = odds.union(evens)
print(union)

print("\nIntersection will only take elements that are present in both sets using intersection(). It will generate"
      " an empty set if there are none.")
intersection = odds.intersection(evens)
print(intersection)
intersection = odds.intersection(primes)
print(intersection)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

print("\nUsing .diff() will show the difference between the two sets and only take elements that are only present"
      " in the first set.")
diff = setA.difference(setB)
print(diff)

print("\nSymmetric difference, .symmetric_difference(), will take the elements that are not present in the other set.")
diff = setA.symmetric_difference(setB)
print(diff)

print("\nUsing union, intersection, and difference will not modify the original sets, only generate a new one. To modify"
      " original sets, must use .update().")
setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 7, 8, 9}

print("\nUsing .intersection_update() will modify a set to only contain elements that are in both sets.")
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 7, 8, 9}

print("\nUsing .difference_update() will remove any elements that are found in another set.")
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 7, 8, 9}

print("\nUsing .symmetric_difference_update() will keep the elements only found in one set and remove any elements that "
      "are found in both.")
setA.symmetric_difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print("\nIt is possible to find out whether a set is a subset of another set, i.e. all the elements in one set are "
      "in the other set, using .issubset(). It will return a Boolean value.")
print(setA.issubset(setB))

print("\nIt is possible to find out whether a set is a superset, i.e. contains all the elements in the other set, using "
      ".issuperset(). Returns a Boolean value.")
print(setA.issuperset(setB))

print("\nIt is possible to find out if two sets are disjointed, i.e. they have no common values, using .isdisjoint().")
print(setA.isdisjoint(setB))
setC = {7, 8, 9}
print(setA.isdisjoint(setC))

print("\nLike with Lists and Dicts, trying to generate a copy by just setting them equal to each other just copies the"
      " reference point, thus changing something in one set will change the other. In order to generate an actual"
      " copy, must use .copy().")
setB = setC.copy()
print(setB)

print("\nIt is also possible to use set() to generate a copy.")
setB = set(setA)
print(setB)

print("\nIt is possible to create an immutable set by using .frozenset(). Union, difference, intersect will still work.")
mySet = frozenset(setA)
print(mySet)