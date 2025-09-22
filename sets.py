# Sets:- unordered collection of unique elements , it is mutable , No duplicates-> automatically
# removed duplicate values , fast membership testing , holds unique elements , elements must be 
# hashable , mathematical set operation(union , intersection , etc.)


# if there is no elements inside the curly brackets {} then interpreter will asume it to be dictionary.
#Creating a set:
my_set = {1,2,3,2,3,4}
print(my_set)

# Creating an Empty Set:
my_set_2 = set()
print(my_set_2)

#Type of my Set:
print(type(my_set_2))

# Sets of strings
set_strings={'Ferrari' , 'Maruti' , 'RangeRover' , 'Omni Van' ,'Rolling'}
print(set_strings)

# Set from a list:
set_from_list = set([1,2,3,2,3,2,3,23])
print(set_from_list)

#Set from the string:
set_from_string= set(["Varad"])
print(set_from_string)

# add a single number instide the set: .add()
my_set.add(5)
print(my_set)

# Add multiple elements in the set 
my_set.update(["Varad","2007"])
print(my_set)

#Remove the element from the set : .remove() method!
my_set.remove(2)
print(my_set)

# Discard :- removes the element passed: do not give error if key is not ther 
my_set.discard('591')
print(my_set)

# pop(): removes the arbitrary element from the set
my_set.pop()
print(my_set)

#clear() : remove all the elements from the set
my_set.clear()
print(my_set)
my_set.add(0)
#Membership operator in set: in , not in : relatively efficient (faster)
print(0 in my_set)
print(0 not in my_set)

# Calculating the size of the set: len()
print(len(my_set))

for item in my_set:
    print(item, end=" ")