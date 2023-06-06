
# MAP & FILTERS

The built-in functions **map** and **filter** are very useful higher-order functions that operate on lists (or similar objects called iterables).
The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

Встроенные функции **map** и **filter** — это очень полезные функции высшего порядка, которые работают со списками (или подобными объектами, называемыми итерируемыми).
Функций **map** принимает функцию и итерируемый объект в качестве аргументов и возвращает новый итерируемый объект с функцией, примененной к каждому аргументу.

**Example:**
	def add_five(x):
    	    return x + 5

	nums = [11, 22, 33, 44, 55]
	result = list(map(add_five, nums))
	print(result)

> Hint: Better use lambda function
> Hint: To convert the result into a list, we used list explicitly.

## Filter

The function **filter** filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).

Функция **filter** фильтрует итерируемый объект, удаляя элементы, не соответствующие предикату (функция, возвращающая логическое значение).

**Example:**

	nums = [11, 22, 33, 44, 55]
	res = list(filter(lambda x: x%2==0, nums))
	print(res)
	# Output is list with even numbers

> Hint: Like **map**, the result has to be explicitly converted to a list if you want to print it.


