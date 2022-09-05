#Data Structures
'''
What are Data structures?
Data Structures allows you to organize our data in such a way that enables us to store collections of data,
relate them and perform operations on them accordingly.

Types of Data Structures in Python
a.Builtin data structures
b.user defined data structures
Python has implicit support for Data Structures which enable us to store and access data.

 a.Types of builtin data structures are:

 1.List

 2.Tuple

 3.Set

 4.Dictionary

1.List
 Lists are used to store data of different data types in a sequential manner.
 There are addresses assigned to every element of the list, which is called as Index.
 The index value starts from 0 and goes on until the last element called the positive index.
 There is also negative indexing which starts from -1 enabling you to access elements from the last to first.

Let us now understand lists better with the help of an example program.

1.1 Creating a list

To create a list, you use the square brackets and add elements into it accordingly.
If you do not pass any elements inside the square brackets, you get an empty list as the output.
 '''
empty_list = [] #create empty list
print(empty_list)
empty_list = [100, 200, 30, 'any data type', 3.148] #creating list with data
print(empty_list)
#Output:
#[]
#[100, 200, 30, 'any data type', 3.148]
'''
1.2 Adding Elements

Adding the elements in the list can be achieved using the append(), extend() and insert() functions.

The append() function adds all the elements passed to it as a single element.
The extend() function adds the elements one-by-one into the list.
The insert() function adds the element passed to the index value and increase the size of the list too.
'''
#Example:
x_list = [1, 2, 3,4]
print(x_list)
x_list.append([22, 82]) #add as a single element
print(x_list)
x_list.extend([523, 'Cars']) #add as different elements
print(x_list)
x_list.insert(1, 'inserted_string') #add element i
print(x_list)

#Output:
#[1, 2, 3,4]
#[1, 2, 3, [22, 82]]
#[1, 2, 3, [22, 82], 523, ‘Cars’]
#[1, ‘insert_string’, 2, 3,4, [22, 82], 523, ‘Cars’]
'''

1.3 Deleting Elements
To delete elements, use the del keyword which is built-in into Python but this does not return anything back to us.
If we want the element back, we can use the pop() function which takes the index value.
To remove an element by its value, we can use the remove() function.
Example:
'''
y_list =[1,'insert_string',2,3,4,[22, 82],523,'Cars']
del y_list[4] #delete element at index 4
print(y_list)
y_list.remove('Cars') #remove element with value
print(y_list)
a = y_list.pop(1) #pop element from list
print('Popped Element: ', a, ' List remaining: ', y_list)
y_list.clear() #empty the list

#Output:
#[1, 'insert_string', 2, 3, [22, 82], 523, 'Cars']
#[1, 'insert_string', 2, 3, [22, 82], 523]
#Popped Element:  insert_string  List remaining:  [1, 2, 3, [22, 82], 523]


'''
1.4 Accessing Elements
Accessing elements is the same as accessing Strings in Python. 
we can pass the index values and hence can obtain the values as needed.

'''
z_list = [1,2,3,[22, 82],523]
for element in z_list: #access elements one by one
    print(element)
print(z_list) #access all elements
print(z_list[3]) #access index 3 element
print(z_list[0:2]) #access elements from 0 to 1 and exclude 2
print(z_list[::-1]) #access elements in reverse
'''
Output:
1
2
3
[22, 82]
523
[1, 2, 3, [22, 82], 523]
[22, 82]
[1, 2]
[523, [22, 82], 3, 2, 1]

2.Tuples

Tuples are the same as lists are with the exception that the data once entered into the tuple cannot be changed no matter what. 
The only exception is when the data inside the tuple is mutable, only then the tuple data can be changed. 

2.1 Creating a Tuple

We can create a tuple using parenthesis or using the tuple() function.
Example:
'''
a_tuple = (9,4,8) #create tuple
print(a_tuple)
#Output:
#(9,4,8)

#2.2 Accessing Elements
#Accessing elements is the same as it is for accessing values in lists.
#Example:

b_tuple = (9, 4, 8, 'chetan') #access elements
for x in b_tuple:
    print(x)
print(b_tuple)
print(b_tuple[0])
print(b_tuple[:])
print(b_tuple[3][4])
'''
Output:
9
4
8
chetan
(9, 4, 8, 'chetan')
9
(9, 4, 8, 'chetan')
a
'''
#2.3 Appending Elements
#To append the values, you use the ‘+’ operator which will take another tuple to be appended to it.
#Example:
c_tuple = (9,4,8)
c_tuple = c_tuple + (0,1,2) #add elements
print(c_tuple)

#Output:
#(9,4,8,0,1,2)

'''
3.Sets

Sets are a collection of unordered elements that are unique. Meaning that even if the data is repeated more than one time, 
it would be entered into the set only once. 
The operations also are the same as is with the arithmetic sets. 

3.1 Creating a set
Sets are created using the flower braces but instead of adding key-value pairs, you just pass values to it.
Example
'''
d_set = {9,6,4,2,3,3,3,1,6} #create set
print(d_set)

#Output:
#{9,6,4,2,3,1,6}

#3.2 Adding elements
#To add elements, you use the add() function and pass the value to it.
e_set = {3, 2, 1}
e_set.add(0) #add element to set
print(e_set)
#Output:
#{3,2,1,0}

#3.3 Operations in sets
#The different operations on set such as union, intersection and so on are shown below.
#The union() function combines the data present in both sets.
#The intersection() function finds the data present in both sets only.
#The difference() function deletes the data present in both and outputs data present only in the set passed.
#The symmetric_difference() does the same as the difference() function but outputs the data which is remaining in both sets.
#Example
a1_set = {9, 4, 8, 2}
a2_set = {0, 2, 6, 11}
print(a1_set.union(a2_set), '----------', a1_set | a2_set)
print(a1_set.intersection(a2_set), '----------', a1_set & a2_set)
print(a1_set.difference(a2_set), '----------', a1_set - a2_set)
print(a1_set.symmetric_difference(a2_set), '----------', a1_set ^ a2_set)
a1_set.clear()
print(a1_set)
#Output
#{0, 2, 4, 6, 8, 9, 11} ---------- {0, 2, 4, 6, 8, 9, 11}
#{2} ---------- {2}
#{8, 9, 4} ---------- {8, 9, 4}
#{0, 4, 6, 8, 9, 11} ---------- {0, 4, 6, 8, 9, 11}
#set()
'''
4.Dictionary
Dictionaries are used to store key-value pairs. 
Python dictionary is an unordered collection of items.
Dictionaries are optimized to retrieve values when the key is known.

4.1 Creating a Dictionary
Dictionaries can be created using the flower braces or using the dict() function. 
We need to add the key-value pairs whenever we work with dictionaries.
'''
#Example

g_dict = {} #empty dictionary
print(g_dict)
g_dict = {1: 'chetan', 2: 'chandan',3:'chirag'} #dictionary with elements
print(g_dict)

#Output:
#{}
#{1: 'chetan', 2: 'chandan',3:'chirag'}
'''
4.2 Changing and Adding key, value pairs
To change the values of the dictionary, we need to do that using the keys. 
So, we firstly access the key and then change the value accordingly. 
To add values, we simply just add another key-value pair as shown below.
'''
Cars_dict = {'First': 'Chiron', 'Second': 'Veyron','Third': 'Aventodor','Fourth': 'A8'}
print(Cars_dict)
Cars_dict['Second'] = 'Urus' #changing element
print(Cars_dict)
Cars_dict['Third'] = 'Portofino' #adding key-value pair
print(Cars_dict)

#Output:
#{'First': 'Chiron', 'Second': 'Veyron', 'Third': 'Aventodor', 'Fourth': 'A8'}
#{'First': 'Chiron', 'Second': 'Urus', 'Third': 'Aventodor', 'Fourth': 'A8'}
#{'First': 'Chiron', 'Second': 'Urus', 'Third': 'Portofino', 'Fourth': 'A8'}
'''
4.3 Deleting key, value pairs
To delete the values, you use the pop() function which returns the value that has been deleted.
To retrieve the key-value pair, you use the popitem() function which returns a tuple of the key and value.
To clear the entire dictionary, you use the clear() function.
'''
#Example
cars1_dict = {'Bugatti': 'Chiron', 'Lamborghini': 'Urus', 'Ferrari': 'Portofino', 'Audi': 'A8'}
a = cars1_dict.pop('Lamborghini') #pop element
print('Value:', a)
print('Dictionary:', cars1_dict)
b = cars1_dict.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', cars1_dict)
cars1_dict.clear() #empty dictionary
print('n', cars1_dict)

#Output:
#Value: Urus
#Dictionary: {'Bugatti': 'Chiron', 'Ferrari': 'Portofino', 'Audi': 'A8'}
#Key, value pair: ('Audi', 'A8')
#Dictionary {'Bugatti': 'Chiron', 'Ferrari': 'Portofino'}
#Empty: {}

#4.4 Other Functions
# We have different functions which return to us the keys or the values of the key-value pair accordingly to the
# keys(), values(), items() functions accordingly.

#Example
my_cars = {'Bugatti': 'Chiron', 'Lamborghini': 'Urus', 'Ferrari': 'Portofino', 'Audi': 'A8'}
print(my_cars.keys()) #get keys
print(my_cars.values()) #get values
print(my_cars.items()) #get key-value pairs
print(my_cars.get('First'))

#Output:
#dict_keys(['Bugatti', 'Lamborghini', 'Ferrari', 'Audi'])
#dict_values(['Chiron', 'Urus', 'Portofino', 'A8'])
#dict_items([('Bugatti', 'Chiron'), ('Lamborghini', 'Urus'), ('Ferrari', 'Portofino'), ('Audi', 'A8')])
#Chiron
