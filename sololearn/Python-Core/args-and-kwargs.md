
## *args 

Python allows you to have functions with varying numbers of arguments.

Using ***args** as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.

Python позволяет вам иметь функции с различным количеством аргументов.

Использование ***args** в качестве параметра функции позволяет передать произвольное количество аргументов этой функции. Аргументы затем доступны как аргументы кортежа в теле функции.

	def function(named_arg, *args):
        print(named_arg)
        print(args)
        
    function(1, 2, 3, 4, 5, 6)
      
	# Output is 1 and tuple(2, 3, 4, 5, 6)

> Hint: The parameter *args must come after the named parameters to a function.
The name args is just a convention; you can choose to use another.

> Подсказка: Параметр *args должен стоять после именованных параметров функции.
Имя args — это просто соглашение; вы можете использовать другой.

## **kwargs


****kwargs** (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.

The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.

****kwargs** (расшифровывается как аргументы ключевого слова) позволяет вам обрабатывать именованные аргументы, которые вы не определили заранее.

Аргументы ключевого слова возвращают словарь, в котором ключи — это имена аргументов, а значения — значения аргументов.


	def my_func(x, y=7, *args, **kwargs):
        print(x)
        print(y)
        print(args)
        print(kwargs)
        
    my_func(2, 3, 4, 5, 6, a=7, b=8)
    
    # Output is 2, 3, (4, 5, 6), {'a': 7, 'b': 8} spacec instead of ,


**a** and **b** are the names of the arguments that we passed to the function call.

**a** и **b** — имена аргументов, которые мы передали вызову функции.

> Hint: The arguments returned by **kwargs are not included in *args.

> Подсказка: аргументы, возвращаемые **kwargs, не включаются в *args.

