
# Decorators

## Decorators

**Decorators** provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions that you don't want to modify.

**Декораторы** позволяют изменять функции с помощью других функций.
Это идеально, когда вам нужно расширить функциональность функций, которые вы не хотите изменять.

**Example:**

	def decor(func):
  	    def wrap():
    	    print("============")
            func()
    	    print("============")
  	return wrap
	
	def print_text():
  	    print("Hello world!")

	decorated = decor(print_text)
	decorated()


We defined a function named **decor** that has a single parameter func. Inside decor, we defined a nested function named **wrap**.
The **wrap** function will print a string, then call func(), and print another string. The decor function returns the **wrap** function as its result.
We could say that the variable decorated is a decorated version of print_text - it's print_text plus something.
In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version altogether so we always got our "plus something" version of print_text.
This is done by re-assigning the variable that contains our function:	

Мы определили функцию **decor** с одним параметром func. Внутри декора мы определили вложенную функцию с именем **wrap**.
Функция **wrap** напечатает строку, затем вызовет func() и напечатает другую строку. Функция decor возвращает в качестве результата функцию **wrap**.
Можно сказать, что декорированная переменная — это декорированная версия print_text — это print_text плюс что-то еще.
На самом деле, если бы мы написали полезный декоратор, мы могли бы вообще заменить print_text на декорированную версию, чтобы мы всегда получали нашу версию print_text с добавлением чего-то.
Это делается путем переназначения переменной, содержащей нашу функцию:

**Example 2:**

	def decor(func):
    	    def wrap():
                print("============")
        	func()
        	print("============")
    	    return wrap

	def print_text():
    	    print("Hello world!")

	print_text = decor(print_text)
	print_text()

> Hint: Now print_text corresponds to our decorated version.


## Decorators

In our previous example, we decorated our function by replacing the variable containing the function with a wrapped version.

В нашем предыдущем примере мы украсили нашу функцию, заменив переменную, содержащую функцию, обернутой версией.

	def decor(func):
    	    def wrap():
        	print("============")
        	func()
        	print("============")
    	    return wrap

	def print_text():
    	    print("Hello world!")

	print_text = decor(print_text)
	print_text()


This pattern can be used at any time, to wrap any function.
Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
If we are defining a function we can "decorate" it with the @ symbol like:

Этот шаблон можно использовать в любое время, чтобы обернуть любую функцию.
Python поддерживает перенос функции в декоратор, добавляя перед определением функции имя декоратора и символ @.
Если мы определяем функцию, мы можем «украсить» ее символом @

**Same example for first code**

	def decor(func):
    	    def wrap():
        	print("============")
        	func()
        	print("============")
    	    return wrap

	@decor
	def print_text():
    	    print("Hello world!")

	print_text()

> Hint: A single function can have multiple decorators.

