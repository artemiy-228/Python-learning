
# Python Data Structures

Almost every program uses data.
Organizing, managing and storing data is important as it enables easier access and efficient modifications.

Data Structures allow you to store and manage your data.

Python has a number of built-in data structures:

	
* Strings
* Lists
* Dictionaries
* Tuples
* Sets

In addition to the built-in data structures, Python allows you to create your own data structures,
 enabling you to have full control over their functionality.

The most prominent data structures are:

* Stacks
* Queues
* Trees
* Linked Lists


# Strings

Strings are used to store text, and are one of the simplest and most used data structures.

Any text between two single or double quotation marks is a string.

### Special Character

* \n represents a new line
* \t represents tab

Hint: The backslash is also called the escape character

## Accessing Strings

Strings can be thought of as a sequence of characters. Each character in the string has its unique position (or index).

You can access a character of a string using its index:

	print(line[0])

You can also use negative indices, which access the characters of the string counting from the end.

	print(line[-1])


## String Operations

The in operator can be used to check if a string is part of another string.

Strings can be added together (also called concatenation) and also be multiplied by integers

	 "abra" + "cadabra" = "abracadabra"
	 "abra" * 3 = "abraabraabra"

## String Functions

String have many useful functions:
* **count(str)** -  returns how many times the str substring appears in the given string.
* **upper()** -  converts the string to uppercase.
* **lower()** -  converts the string to lowercase.
* **replace(old, new)** -  replaces all occurrences of old with new.
* **len(str)** -  returns the length of the string (number of characters).


# Lists


Lists are used to store multiple elements, each corresponding to an index.

They are created using square brackets.
	list = ["word1", "word2", "word3"]
The names list contains three strings. Each element of the list can be accessed using its index
	print(list[1])

Lists can be used to represent a collection of data, for example ages of people, monthly growth rates of stocks, etc.

Lists can also be nested to represent 2D grids, such as matrices
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## List Operations

Similar to strings, we can use the in and not in operators to check if an element is part of the list

	words = ["spam", "egg", "spam", "sausage"]
	print("spam" in words)
	print("egg" in words)
	print("tomato" in words)

## List Functions

Lists support the following functions:
* **append(item)** -  adds an item to the end of the list.
* **insert(index, item)** -  adds an item at the given index in the list.
* **remove(item)** -  removes an item from the list.
* **pop(index)** -  removes the item at the given index.
* **count(item)** -  returns a count of how many times an item occurs in the list.
* **reverse()** reverses items in the list.
* **sort()** sorts the list. By default, the list is sorted ascending.
* You can specify reverse=True as the parameter, to sort descending.
* **max(list)** returns the maximum value.
* **min(list)** returns the minimum value.


## List Comprehensions

List comprehensions are a useful way of quickly creating lists whose contents obey a rule.
For example, we can do the following:

	# a list comprehension
	cubes = [i**3 for i in range(5)]
	print(cubes)

A list comprehension can also contain an if statement to enforce a condition on values in the list.
	evens = [i**2 for i in range(10) if i**2 % 2 == 0]
	print(evens)


# Dictionaries

We saw how lists allow us to store elements with their corresponding indices.
The indices in a list are automatically set. But what if we need to set our own index?

**Dictionaries** are another collection type and allow us to map arbitrary keys to values.
**Dictionaries** can be indexed in the same way as lists, using square brackets containing keys.

	ages = {"Dave": 24, "Mary": 42, "John": 58}
	print(ages["Dave"]) Dave - key, 24 - value
	print(ages["Mary"]) Mary - key, 42 - value

You can use strings, integers, booleans, and any other immutable type as dictionary keys.
This means that you cannot use lists or dictionaries as keys

To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list

	nums = {1: "one", 2: "two", 3: "three"}
	print(1 in nums)
	print("three" in nums)
	print(4 not in nums)
	#this check checks for keys, not values

A useful dictionary function is **get()**. It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead.

	pairs = {1: "apple", "orage": [2, 3, 4],  True: False,  12: "True"}

	print(pairs.get("orange", "yellow")) #input yellow
	print(pairs.get(12, 42)) #input True
	print(pairs.get(12345, "not found")) #input not found

# Tuples

Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using **parentheses**, rather than square brackets.
	
	words = ("spam", "eggs", "sausages",)
	print(words[0])

Hint: Like lists and dictionaries, tuples can be nested within each other

An advantage of tuples over lists is that they can be used as keys for dictionaries (because they are immutable)
	dict = { ("David", 42): "red",("Bob", 24): "green"}
	print(dict[("Bob", 24)]) 

Hint: Tuples are faster than lists, but they cannot be changed.

## Tuple Unpacking

**Tuple unpacking** allows you to assign each item in a collection to a variable.

	numbers = (1, 2, 3)
	a, b, c = numbers
	print(a)
	print(b)
	print(c)
	
Hint: This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side forms the tuple (b, a) which is then unpacked.


A variable that is prefaced with an asterisk (*) takes all values from the collection that are left over from the other variables.

	a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(a)
	print(b)
	print(c)
	print(d)

Hint: c will get assigned the values 3 to 8.

# Sets

**Sets** are collections of unordered items that are unique.

They are created using curly braces, and, due to the way they're stored, it's faster to check whether an item is part of a **set** using the in operator, rather than part of a **list**.

	num_set = {1, 2, 3, 4, 5}
	print(0 in num_set) #False
	print(1 in num_set) #True

Hint: **Sets cannot contain duplicate elements**.

## Sets useful functions

You can use the **add()** function to add new items to the set, and **remove()** to delete a specific element

	nums = {1, 2, 1, 3, 1, 4, 5, 6}
	print(nums)
	nums.add(-7)
	nums.remove(3)
	print(nums)

Hint: Duplicate elements will automatically get removed from the set.

## Sets and bool algebra

Sets can be combined using mathematical operations.
* The **union** operator **|** combines two sets to form a new one containing items in either.
* The **intersection** operator **&** gets items only in both.
* The **difference** operator **-** gets items in the first set but not in the second.
* The **symmetric** difference operator **^** gets items in either set, but not both.

	first = {1, 2, 3, 4, 5, 6}
	second = {4, 5, 6, 7, 8, 9}

	print(first | second) #Input - {1, 2, 3, 4, 5, 6, 7, 8, 9}
	print(first & second) #Input - {4, 5, 6}
	print(first - second) #Input - {1, 2, 3}
	print(second - first) #Input - {8, 9, 7}
	print(first ^ second) #Input - {1, 2, 3, 7, 8, 9}

