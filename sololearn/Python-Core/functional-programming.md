<h1 style="text-aligh: center">Functional Programming</h1>

**Functional programming** is a style of programming that (as the name suggests) is based around **functions**.
A key part of **functional programming** is higher-order **functions**. We have seen this idea briefly in the previous lesson on **functions** as objects.
Higher-order **functions** take other **functions** as arguments, or return them as results.


**Функциональное программирование** — это стиль программирования, который (как следует из названия) основан на **функциях**.
Ключевой частью **функционального программирования** являются **функции высшего порядка**. Мы кратко рассмотрели эту идею в предыдущем уроке о **функциях** как объектах.
**Функции высшего порядка** принимают другие **функции** в качестве аргументов или возвращают их в качестве результатов.

**Example:**

	def apply_twice(func, arg):
    	    return func(func(arg))

	def add_five(x):
    	    return x + 5

	print(apply_twice(add_five, 10))

Hint: The function **apply_twice()** takes another function as its argument, and calls it twice inside its body.


<h1 style="text-aligh: center">Pure Functions</h1>

**Functional programming** seeks to use **pure functions**. **Pure functions** have no side effects, and return a value that depends only on their arguments.
This is how **functions** in math work: for example, The **cos(x)** will, for the same value of x, always return the same result.
Below are examples of pure and impure **functions**.


**Функциональное программирование** стремится использовать **чистые функции**. **Чистые функции** не имеют побочных эффектов и возвращают значение, которое зависит только от их аргументов.
Вот как работают **функции** в математике: например, **cos(x)** для одного и того же значения x всегда будет возвращать один и тот же результат.
Ниже приведены примеры чистых и нечистых **функций**.

**Pure function**:

	def pure_function(x, y):
	    temp = x + 2*y
	    return temp / (2*x + y)

**Impure function.**
	
	some_list = []

	def impure(arg):
	    some_list.append(arg)

Hint: 
The function above is not pure, because it changed the state of **some_list()**.


<h1 style="text-aligh: center"><h1>Pure Functions +/-</h1>

Using pure functions has both advantages and disadvantages.

**Pure functions are:**

- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed,
 reducing the number of times the function is called. This is called **memoization**.
- easier to run in parallel.

Использование чистых функций имеет как преимущества, так и недостатки.

**Чистые функции это:**

- легче рассуждать и тестировать.
- более эффективным. После того, как функция была оценена для ввода, результат может быть сохранен и использован в следующий раз, когда функция этого ввода потребуется,
 что сократит количество вызовов функции. Это называется мемоизация.
- легче работать параллельно.

**Disadvantage**

The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O,
since this appears to inherently require side effects.
They can also be more difficult to write in some situations.


**Недостаток**

Основным недостатком использования только чистых функций является то, что они значительно усложняют простую в остальном задачу ввода-вывода,
поскольку это, по-видимому, требует побочных эффектов.
Их также может быть сложнее написать в некоторых ситуациях.

