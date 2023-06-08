
<center><h1> Python Data Structures</h1></center>

Almost every program uses data.
Organizing, managing and storing data is important as it enables easier access and efficient modifications.

Data Structures allow you to store and manage your data.

Python has a number of built-in data structures:

	
* **Strings**
* **Lists**
* **Dictionaries**
* **Tuples**
* **Sets**

In addition to the built-in data structures, Python allows you to create your own data structures,
 enabling you to have full control over their functionality.

The most prominent data structures are:

* **Stacks**
* **Queues**
* **Trees**
* **Linked Lists**


# Strings

**Strings** are used to store text, and are one of the simplest and most used data structures.

Any text between two single or double quotation marks is a **string**.

### Special Character

* **\n** represents a new line
* **\t** represents tab

Hint: The backslash is also called the escape character

## Accessing Strings

**Strings** can be thought of as a sequence of characters. Each character in the **string** has its unique position (or index).

You can access a character of a **string** using its index:

	print(line[0])

You can also use negative indices, which access the characters of the **string** counting from the end.

	print(line[-1])


## String Operations

The in operator can be used to check if a string is part of another **string**.

**Strings** can be added together (also called concatenation) and also be multiplied by **integers**

	 "abra" + "cadabra" = "abracadabra"
	 "abra" * 3 = "abraabraabra"

## String Functions

**String** have many useful functions:
* **count(str)** -  returns how many times the str substring appears in the given **string**.
* **upper()** -  converts the **string** to uppercase.
* **lower()** -  converts the **string** to lowercase.
* **replace(old, new)** -  replaces all occurrences of old with new.
* **len(str)** -  returns the length of the **string** (number of characters).


# Lists


**Lists** are used to store multiple elements, each corresponding to an index.

They are created using square brackets.
	list = ["word1", "word2", "word3"]
The names **list** contains three **strings**. Each element of the **list** can be accessed using its index
	print(list[1])

**Lists** can be used to represent a collection of data, for example ages of people, monthly growth rates of stocks, etc.

**Lists** can also be nested to represent 2D grids, such as matrices
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## List Operations

Similar to **strings**, we can use the in and not in operators to check if an element is part of the **list**

	words = ["spam", "egg", "spam", "sausage"]
	print("spam" in words)
	print("egg" in words)
	print("tomato" in words)

## List Functions

**Lists** support the following functions:
* **append(item)** -  adds an item to the end of the **list**.
* **insert(index, item)** -  adds an item at the given index in the **list**.
* **remove(item)** -  removes an item from the **list**.
* **pop(index)** -  removes the item at the given index.
* **count(item)** -  returns a count of how many times an item occurs in the **list**.
* **reverse()** reverses items in the **list**.
* **sort()** sorts the **list**. By default, the **list** is sorted ascending.
* You can specify reverse=True as the parameter, to sort descending.
* **max(list)** returns the maximum value.
* **min(list)** returns the minimum value.


## List Comprehensions

**List** comprehensions are a useful way of quickly creating **lists** whose contents obey a rule.
For example, we can do the following:

	# a list comprehension
	cubes = [i**3 for i in range(5)]
	print(cubes)

A **list** comprehension can also contain an if statement to enforce a condition on values in the **list**.
	evens = [i**2 for i in range(10) if i**2 % 2 == 0]
	print(evens)


# Dictionaries

We saw how **lists** allow us to store elements with their corresponding indices.
The indices in a **list** are automatically set. But what if we need to set our own index?

**Dictionaries** are another collection type and allow us to map arbitrary **keys** to **values**.
**Dictionaries** can be indexed in the same way as **lists**, using square brackets containing **keys**.

	ages = {"Dave": 24, "Mary": 42, "John": 58}
	print(ages["Dave"]) Dave - key, 24 - value
	print(ages["Mary"]) Mary - key, 42 - value

You can use **strings, integers, booleans**, and any other immutable type as **dictionary keys**.
This means that you cannot use **lists** or **dictionaries** as **keys**

To determine whether a **key** is in a **dictionary**, you can use in and not in, just as you can for a **list**

	nums = {1: "one", 2: "two", 3: "three"}
	print(1 in nums)
	print("three" in nums)
	print(4 not in nums)
	#this check checks for keys, not values

A useful **dictionary** function is **get()**. It does the same thing as indexing, but if the **key** is not found in the **dictionary** it returns another specified **value** instead.

	pairs = {1: "apple", "orage": [2, 3, 4],  True: False,  12: "True"}

	print(pairs.get("orange", "yellow")) #input yellow
	print(pairs.get(12, 42)) #input True
	print(pairs.get(12345, "not found")) #input not found

# Tuples

**Tuples** are very similar to **lists**, except that they are immutable (they cannot be changed).
Also, they are created using **parentheses**, rather than square brackets.
	
	words = ("spam", "eggs", "sausages",)
	print(words[0])

Hint: Like **lists** and **dictionaries**, **tuples** can be nested within each other

An advantage of **tuples** over **lists** is that they can be used as **keys** for **dictionaries** (because they are immutable)
	dict = { ("David", 42): "red",("Bob", 24): "green"}
	print(dict[("Bob", 24)]) 

Hint: **Tuples** are faster than **lists**, but they cannot be changed.

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

You can use the **add()** function to add new items to the **set**, and **remove()** to delete a specific element

	nums = {1, 2, 1, 3, 1, 4, 5, 6}
	print(nums)
	nums.add(-7)
	nums.remove(3)
	print(nums)

Hint: Duplicate elements will automatically get removed from the **set**.

## Sets and bool algebra

**Sets** can be combined using mathematical operations.
* The **union** operator **|** combines two **sets** to form a new one containing items in either.
* The **intersection** operator **&** gets items only in both.
* The **difference** operator **-** gets items in the first **set** but not in the second.
* The **symmetric** difference operator **^** gets items in either **set**, but not both.

	first = {1, 2, 3, 4, 5, 6}
	second = {4, 5, 6, 7, 8, 9}

	print(first | second)
        #Input - {1, 2, 3, 4, 5, 6, 7, 8, 9}

	print(first & second)
        #Input - {4, 5, 6}

	print(first - second)
        #Input - {1, 2, 3}

	print(second - first)
        #Input - {8, 9, 7}

	print(first ^ second)
        #Input - {1, 2, 3, 7, 8, 9}

# Data Structures - Summary ENG/RUS (for repeat)

As we have seen in the previous paragraphs, Python supports the following collection types: **Lists**, **Dictionaries**, **Tuples**, **Sets**.

Here are some general guidelines for choosing the correct data structure:
- Use a **dictionary**, when you need a logical association between a **key:value**
  Используйте **словарь**, когда вам нужна логическая связь между **ключом: значением**

- Use **lists** if you have a collection of data that does not need random access. Try to choose **lists** when you need a simple, iterable collection that is modified frequently.
  Используйте **списки**, если у вас есть коллекция данных, не требующая произвольного доступа. Старайтесь выбирать **списки**, когда вам нужна простая итерируемая коллекция, которая часто изменяется.

- Use a **set** if you need uniqueness for the elements.
  Используйте **Множества**, если вам нужна уникальность элементов.

- Use **tuples** when your data cannot/should not change.
  Используйте **кортежи**, когда ваши данные не могут/не должны изменяться.

Hint: Many times, a **tuple** is used in combination with a **dictionary**, for example, a **tuple** can represent a **key**, because it's immutable.

      Часто **кортеж** используется в сочетании со **словарем**, например, **кортеж** может представлять **ключ**, потому что он неизменяем.


<center><h1>User-Defined Data Structures</h1></center>

In the previous modules we have seen the built-in data structures in Python, which include **Lists**, **Dictionaries**, **Tuples** and **Sets**.

Some applications require additional functionality when working with data, for example, word processors have an undo-redo function, task schedulers need queuing mechanisms, maps need to find the shortest path, etc.
In these cases we need to define our own data structures that provide the required functionality.

Some of the most popular data structures are:
- Stacks
- Queues
- Linked Lists
- Graphs

Hint: We will implement the above data structures and use them to solve popular problems.

# Stack

A stack is a simple data structure that adds and removes elements in a particular order.
Every time an element is added, it goes on the "top" of the stack. Only an element at the top of the **stack** can be removed, just like a stack of plates. This behavior is called **LIFO** (Last In, First Out).

Стек — это простая структура данных, которая добавляет и удаляет элементы в определенном порядке.
Каждый раз, когда добавляется элемент, он помещается на «верх» стека. Только элемент в верхней части **стека** может быть удален, как стопка тарелок. Такое поведение называется **LIFO** (последним пришел, первым ушел).

**Terminology**
Adding a new element onto the stack is called **push**.
Removing an element from the stack is called **pop**.

**Терминология**
Добавление нового элемента в стек называется **push**.
Удаление элемента из стека называется **pop**.

**Applications**
**Stacks** can be used to create undo-redo functionalities, parsing expressions (infix to postfix/prefix conversion), and much more.

**Приложения**
**Стеки** можно использовать для создания функций отмены и повтора, синтаксического анализа выражений (преобразование инфикса в постфикс/префикс) и многого другого.

Hint: A stack can be implemented using a list in Python.

# Stack in Python

Let's define and implement the Stack class with its corresponding **push, pop, is_empty** and **print_stack** methods.
We will use a **list** to store the data.

Давайте определим и реализуем класс Stack с соответствующими методами **push, pop, is_empty** и **print_stack**.
Мы будем использовать **список** для хранения данных.

**Example:**

	class Stack:
            def __init__(self):
                self.items = []  
  
            def is_empty(self):
                return self.items == []
  
            def push(self, item):
                self.items.insert(0, item)
    
            def pop(self):
                return self.items.pop(0)
    
    	    def print_stack(self):
                print(self.items)
    
	s = Stack()
	s.push('a')
	s.push('b')
	s.push('c')
	s.print_stack()

	s.pop()
	s.print_stack()

	# Output ['c', 'b', 'a']
	# Output ['b', 'a']


> Hint: It's not nessesary to use class. You can work with stack just with lists functions pop and insert.Hint: It's not necessary to use class. You can work with stack just with lists functions pop and insert.

As you can see, it's easy to create a stack using a list.
We use a list called **items** to store our elements.
The **push** method adds an element at the beginning of the list, while the **pop** method removes the first element of the list.

Как видите, стек легко создать с помощью списка.
Мы используем список под названием **items** для хранения наших элементов.
Метод **push** добавляет элемент в начало списка, а метод **pop** удаляет первый элемент списка.


