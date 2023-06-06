
# Recursion

## Recursion


**Recursion** is a very important concept in functional programming.
The fundamental part of recursion is self-reference - functions calling themselves. It is used to solve problems that can be broken up into easier sub-problems of the same type.

A classic example of a function that is implemented recursively is the factorial function, which finds the product of all positive integers below a specified number.
For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!.
Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials.
Below is a recursive implementation of the factorial function.

**Рекурсия** — очень важная концепция функционального программирования.
Фундаментальной частью рекурсии является самоссылка — функции, вызывающие самих себя. Он используется для решения проблем, которые можно разбить на более простые подзадачи того же типа.

Классическим примером рекурсивно реализованной функции является функция факториала, которая находит произведение всех положительных целых чисел, меньших заданного числа.
Например, 5! (5 факториал) это 5 * 4 * 3 * 2 * 1 (120). Чтобы реализовать это рекурсивно, обратите внимание, что 5! = 5*4!, 4! = 4 * 3!, 3! = 3 * 2! и так далее. В общем, н! = n * (n-1)!.
Кроме того, 1! = 1. Это известно как базовый случай, поскольку его можно вычислить без дополнительных факториалов.
Ниже приведена рекурсивная реализация функции факториала.

**Example:**

	def factorial(x):
    	    if x == 1:
        	return 1
            else: 
                return x * factorial(x-1)

	print(factorial(5))

> Hint: The base case acts as the exit condition of the recursion.


**Recursion**

**Recursive** functions can be infinite, just like infinite while loops. These often occur when you forget to implement the base case.
Below is an incorrect version of the **factorial** function. It has no base case, so it runs until the interpreter runs out of memory and crashes.

**Рекурсивные** функции могут быть бесконечными, как и бесконечные циклы while. Это часто происходит, когда вы забываете реализовать базовый случай.
Ниже приведена неправильная версия функции **factorial**. У него нет базового регистра, поэтому он работает до тех пор, пока интерпретатор не исчерпает память и не выйдет из строя.

	def factorial(x):
    	    return x * factorial(x-1)

	print(factorial(5))


**Recursion** can also be indirect. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions.

**Рекурсия** также может быть косвенной. Одна функция может вызывать вторую, которая вызывает первую, которая вызывает вторую и так далее. Это может произойти с любым количеством функций.

	def is_even(x):
    	    if x == 0:
                return True
    	    else:
        	return is_odd(x-1)

	def is_odd(x):
    	    return not is_even(x)


	print(is_odd(17))
	print(is_even(23))

