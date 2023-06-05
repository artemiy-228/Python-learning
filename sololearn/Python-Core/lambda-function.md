
# Lambda Functions

Creating a function normally (using def) assigns it to a variable automatically.
This is different from the creation of other objects - such as **strings** and **integers** - which can be created on the fly, without assigning them to a variable.
The same is possible with **functions**, provided that they are created using **lambda** syntax. **Functions** created this way are known as anonymous.
This approach is most commonly used when passing a simple **function** as an argument to another **function**.
The syntax is shown in the next example and consists of the **lambda** keyword followed by a list of arguments, a colon, and the expression to evaluate and return.


При обычном создании функции (используя def) она автоматически присваивается переменной.
Это отличается от создания других объектов, таких как **строки** и **целые числа**, которые можно создавать на лету, не присваивая их переменной.
То же самое возможно с **функциями** при условии, что они созданы с использованием **лямбда**-синтаксиса. **Функции**, созданные таким образом, называются анонимными.
Этот подход чаще всего используется при передаче простой **функции** в качестве аргумента другой **функции**.
Синтаксис показан в следующем примере и состоит из ключевого слова **лямбда**, за которым следует список аргументов, двоеточие и выражение для оценки и возврата.


	def my_func(f, arg):
  	    return f(arg)

	my_func(lambda x: 2*x*x, 5)

Hint: **Lambda functions** get their name from **lambda calculus**, which is a model of computation invented by Alonzo Church.


# Lambda Functions


**Lambda functions** aren't as powerful as **named functions**.
They can only do things that require a single expression - usually equivalent to a single line of code.

**Лямбда-функции** не так эффективны, как **именованные функции**.
Они могут делать только то, что требует одного выражения, обычно эквивалентного одной строке кода.

	#named function
	def polynomial(x):
    	    return x**2 + 5*x + 4
	print(polynomial(-4))

	#lambda
	print((lambda x: x**2 + 5*x + 4) (-4))

Hint: In the code above, we created an anonymous function on the fly and called it with an argument.

# Lambda Functons

**Lambda functions** can be assigned to variables, and used like normal **functions**.

	double = lambda x: x * 2
	print(double(7))

	def double(x):
	    return x * 2
	
	var = double
	print(var(7))

Hint: However, there is rarely a good reason to do this - it is usually better to define a function with def instead.



