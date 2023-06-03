
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

The backslash is also called the escape character

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
* ** append(item)** -  adds an item to the end of the list.
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
