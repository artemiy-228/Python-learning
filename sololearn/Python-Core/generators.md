
# Generators

**Generators** are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with **for** loops.
They can be created using functions and the **yield** statement.

**Генераторы** — это тип итерируемых объектов, таких как списки или кортежи.
В отличие от списков, они не допускают индексации с произвольными индексами, но их все же можно перебирать с помощью циклов **for**.
Их можно создать с помощью функций и оператора **yield**.

**Example:**

	def countdown():
    	    i=5
    	    while i > 0:
                yield i
                i -= 1

	for i in countdown():
    	    print(i)

> Hint 1: You can use it like range or you can be more resourceful

	def countdown():
    	    i="Hello, World!"
    	    while len(i) > 0:
        	yield i
        	i = i[:len(i) - 1]

	for i in countdown():
    	    print(i)


> Hint: The **yield** statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables. 

Due to the fact that they **yield** one item at a time, **generators** don't have the memory restrictions of lists.
In fact, they can be infinite!

Из-за того, что они **выдают** по одному элементу за раз, **генераторы** не имеют ограничений по памяти, как списки.
На самом деле, они могут быть бесконечными!

	def infinite_sevens():
  	    while True:
    	        yield 7
        
	for i in infinite_sevens():
 	   print(i)

> Hint: In short, **generators** allow you to declare a **function** that behaves like an iterator, i.e. it can be used in a for loop.


Finite **generators** can be converted into lists by passing them as arguments to the list function.

Конечные **генераторы** можно преобразовать в списки, передав их в качестве аргументов функции списка

	def numbers(x):
    	    for i in range(x):
       	    	if i % 2 == 0:
           	     yield i

	print(list(numbers(11)))

> Hint: Using **generators** results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage.
 Furthermore, we do not need to wait until all the elements have been generated before we start to use them.

