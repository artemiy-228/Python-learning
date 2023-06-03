
## Python Data Structures

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


## Strings

Strings are used to store text, and are one of the simplest and most used data structures.

Any text between two single or double quotation marks is a string.

### Special Character

* \n represents a new line
* \t represents tab

The backslash is also called the escape character

## Accessing Strings

Strings can be thought of as a sequence of characters. Each character in the string has its unique position (or index).

You can access a character of a string using its index:

	```print(line[0])```

You can also use negative indices, which access the characters of the string counting from the end.

	```print(line[-1])```


## String Operations

The in operator can be used to check if a string is part of another string.

Strings can be added together (also called concatenation) and also be multiplied by integers

	* "abra" + "cadabra" = "abracadabra"
	* "abra" * 3 = "abraabraabra"

## String Functions

String have many useful functions:
* count(str) -  returns how many times the str substring appears in the given string.
* upper() -  converts the string to uppercase.
* lower() -  converts the string to lowercase.
* replace(old, new) -  replaces all occurrences of old with new.
* len(str) -  returns the length of the string (number of characters).
