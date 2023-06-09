
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

***

<center><h1>Strings</h1></center>

**Strings** are used to store text, and are one of the simplest and most used data structures.

Any text between two single or double quotation marks is a **string**.

### Special Character

* **\n** represents a new line
* **\t** represents tab

> Hint: The backslash is also called the escape character

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

***

<center><h1>Lists</h1></center>


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

***

<center><h1>Dictionaries</h1></center>

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

***

<center><h1>Tuples</h1></center>

**Tuples** are very similar to **lists**, except that they are immutable (they cannot be changed).
Also, they are created using **parentheses**, rather than square brackets.
	
	words = ("spam", "eggs", "sausages",)
	print(words[0])

> Hint: Like **lists** and **dictionaries**, **tuples** can be nested within each other

An advantage of **tuples** over **lists** is that they can be used as **keys** for **dictionaries** (because they are immutable)
	dict = { ("David", 42): "red",("Bob", 24): "green"}
	print(dict[("Bob", 24)]) 

> Hint: **Tuples** are faster than **lists**, but they cannot be changed.

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

> Hint: c will get assigned the values 3 to 8.

***

<center><h1>Sets</h1></center>

**Sets** are collections of unordered items that are unique.

They are created using curly braces, and, due to the way they're stored, it's faster to check whether an item is part of a **set** using the in operator, rather than part of a **list**.

	num_set = {1, 2, 3, 4, 5}
	print(0 in num_set) #False
	print(1 in num_set) #True

> Hint: **Sets cannot contain duplicate elements**.

## Sets useful functions

You can use the **add()** function to add new items to the **set**, and **remove()** to delete a specific element

	nums = {1, 2, 1, 3, 1, 4, 5, 6}
	print(nums)
	nums.add(-7)
	nums.remove(3)
	print(nums)

> Hint: Duplicate elements will automatically get removed from the **set**.

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

***

<center><h1>Data Structures - summary</h1></center>

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

> Hint: Many times, a **tuple** is used in combination with a **dictionary**, for example, a **tuple** can represent a **key**, because it's immutable.

 > Hint: Часто **кортеж** используется в сочетании со **словарем**, например, **кортеж** может представлять **ключ**, потому что он неизменяем.

***

<center><h1>User-Defined Data Structures</h1></center>

In the previous modules we have seen the built-in data structures in Python, which include **Lists**, **Dictionaries**, **Tuples** and **Sets**.

Some applications require additional functionality when working with data, for example, word processors have an undo-redo function, task schedulers need queuing mechanisms, maps need to find the shortest path, etc.
In these cases we need to define our own data structures that provide the required functionality.

Some of the most popular data structures are:
- Stacks
- Queues
- Linked Lists
- Graphs

> Hint: We will implement the above data structures and use them to solve popular problems.

***

<center><h1>Stack</h1></center>

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

#### Applications
**Stacks** can be used to create undo-redo functionalities, parsing expressions (infix to postfix/prefix conversion), and much more.

#### Приложения
**Стеки** можно использовать для создания функций отмены и повтора, синтаксического анализа выражений (преобразование инфикса в постфикс/префикс) и многого другого.

> Hint: A stack can be implemented using a list in Python.

## Stack in Python

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

***

<center><h1>Queue</h1></center>

A **queue** is similar to a stack, but defines a different way to add and remove elements.
The elements are inserted from one end, called the **rear**, and deleted from the other end, called the **front**.
This behavior is called **FIFO** (First in First Out).

**Очередь** похожа на стек, но определяет другой способ добавления и удаления элементов.
Элементы вставляются с одного конца, называемого **задним**, и удаляются с другого конца, называемого **передним**.
Такое поведение называется **FIFO** (First in First Out).

**Terminology**
The process of adding new elements into the **queue** is called **enqueue**.
The process of removal of an element from the **queue** is called **dequeue**.

**Терминология**
Процесс добавления новых элементов в **очередь** называется **ставкой в ​​очередь**.
Процесс удаления элемента из **очереди** называется **удалением из очереди**.

#### Applications
**Queues** are used whenever we need to manage objects in order starting with the first one in.
Scenarios include printing documents on a printer, call center systems answering people on hold, and so on.

#### Приложения
**Очереди** используются всякий раз, когда нам нужно управлять объектами по порядку, начиная с первого входящего.
Сценарии включают печать документов на принтере, системы колл-центров, отвечающие на звонки и т. д.

> Hint: Python lists are the easiest way to implement a queue functionality.

***

## Implement Queue with class

Let's implement the Queue class with it's corresponding enqueue, dequeue, is_empty and print methods.
We will use a list to store the elements.

Давайте реализуем класс Queue с соответствующими методами **enqueue**, **dequeue, is_empty** и **print**.
Мы будем использовать список для хранения элементов.

	class Queue:
        def __init__(self):
        	self.items = []

   	    def is_empty(self):
        	return self.items == []

        def enqueue(self, item):
        	self.items.insert(0, item)

        def dequeue(self):
        	return self.items.pop()

        def print_queue(self):
        	print(self.items)

	q = Queue()
	q.enqueue('a')
	q.enqueue('b')
	q.enqueue('42')
	q.print_queue()
	q.dequeue()
	q.print_queue()

>Hint: The **enqueue** method adds an element at the beginning of the list, while the **dequeue** method removes the last element.

***

<center><h1>Linked List</h1></center>

A **linked list** is a sequence of nodes where each node stores its own data and a link to the next node.
One node links to another forming what can be thought of as a linked chain

**Связанный список** — это последовательность узлов, в которой каждый узел хранит свои данные и ссылку на следующий узел.
Один узел соединяется с другим, образуя то, что можно рассматривать как связанную цепочку.

The first node is called the **head**, and it's used as the starting point for any iteration through the list. The last node must have its link pointing to **None** to determine the end of the list.
Unlike stacks and queues, you can insert and remove nodes in any position of the **linked list** (similar to a standard list).

Первый узел называется **head**, и он используется в качестве отправной точки для любой итерации по списку. Последний узел должен иметь ссылку, указывающую на **None**, чтобы определить конец списка.
В отличие от стеков и очередей, вы можете вставлять и удалять узлы в любом месте **связанного списка** (аналогично стандартному списку).

#### Applications
Linked lists are useful when your data is linked. For example when you need undo/redo functionality, the nodes can represent the state with links to the previous and next states. Another example would be a playlist of music, where each clip is linked with the next one.

#### Приложения
Связанные списки полезны, когда ваши данные связаны. Например, когда вам нужна функция отмены/возврата, узлы могут представлять состояние со ссылками на предыдущее и следующее состояния. Другим примером может быть музыкальный плейлист, где каждый клип связан со следующим.

> Hint: Linked lists can also be used to create other data structures, such as **stack, queues** and **graphs**.

## Linked List in Python

Each node will include data and the link to the next node.

Каждый узел будет включать данные и ссылку на следующий узел.

	class Node:
          def __init__(self, data, next):
              self.data = data
              self.next = next 
Now we can create the **LinkedList** class with the corresponding methods:

	class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next
	
	class LinkedList:
	
	    def __init__(self):
            self.head = None  
        
        def add_at_front(self, data):
            self.head = Node(data, self.head)      

        def add_at_end(self, data):
            if not self.head:
                self.head = Node(data, None)
                return
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data, None)

        def get_last_node(self):
            n = self.head
            while(n.next != None):
                n = n.next
            return n.data

        def is_empty(self):
            return self.head == None

        def print_list(self):
            n = self.head
            while n != None:
                print(n.data, end = " => ")
                n = n.next
            print()

    s = LinkedList()
    s.add_at_front(5)
    s.add_at_end(8)
    s.add_at_front(9)
    
    s.print_list()
    print(s.get_last_node())

The **add_at_front()** method adds a new Node as the head of the list and links the previous head to it.
The **add_at_end()** method iterates to the end of the list using a while loop and adds the new node as the link of the last node.

Метод **add_at_front()** добавляет новый узел в начало списка и связывает с ним предыдущий узел.
Метод **add_at_end()** выполняет итерацию до конца списка, используя цикл while, и добавляет новый узел в качестве ссылки на последний узел.

