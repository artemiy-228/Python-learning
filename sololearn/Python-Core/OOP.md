# OOP

## Classes

### Classes / Классы


The focal point of Object Oriented Programming (OOP) are objects, which are created using classes.

The class describes what the object will be, but is separate from the object itself. In other words, a class can be described as an object's blueprint, description, or definition.

You can use the same class as a blueprint for creating multiple different objects. 

Classes are created using the keyword class and an indented block, which contains class methods (which are functions). 

Below is an example of a simple class and its objects. 

В центре объектно-ориентированного программирования (ООП) находятся объекты, которые создаются с использованием классов.

Класс описывает, каким будет объект, но он отделен от самого объекта. Другими словами, класс можно описать как схему, описание или определение объекта.

Вы можете использовать один и тот же класс в качестве схемы для создания нескольких разных объектов.

Классы создаются с использованием ключевого слова class и блока с отступом, который содержит методы класса (которые являются функциями).

Ниже приведен пример простого класса и его объектов.

    class Cat:
      def __init__(self, color, legs):
        self.color = color
        self.legs = legs
        
    felix = Cat("ginger", 4)
    rover = Cat("dog-colored", 4)
    stumpy = Cat("brown", 3)

> Hint: This code defines a class named Cat, which has two attributes: color and legs.Then the class is used to create 3 separate objects of that class.

> Подсказка: этот код определяет класс с именем Cat, который имеет два атрибута: цвет и ноги.Затем класс используется для создания 3 отдельных объектов этого класса.

### __init__ / Конструкторы


The **__init__** method is the most important method in a class. 

This is called when an instance (object) of the class is created, using the class name as a function.

All methods must have **self** as their first parameter, although it isn't explicitly passed, Python adds the **self** argument to the list for you; you do not need to include it when you call the methods. Within a method definition, **self** refers to the instance calling the method.

Instances of a class have **attributes**, which are pieces of data associated with them.
In this example, **Cat** instances have attributes **color** and **legs**. These can be accessed by putting a **dot**, and the attribute name after an instance. 
In an **__init__** method, **self.attribute** can therefore be used to set the initial value of an instance's **attributes**.

Метод **__init__** — самый важный метод в классе.

Это вызывается при создании экземпляра (объекта) класса с использованием имени класса в качестве функции.

Все методы должны иметь **self** в качестве первого параметра, хотя он не передается явно, Python добавляет аргумент **self** в список для вас; вам не нужно включать его при вызове методов. В определении метода **self** относится к экземпляру, вызывающему метод.

Экземпляры класса имеют **атрибуты**, которые представляют собой фрагменты данных, связанных с ними.
В этом примере экземпляры **Cat** имеют атрибуты **color** и **legs**. Доступ к ним можно получить, поставив **точку** и имя атрибута после экземпляра.
Таким образом, в методе **__init__** **self.attribute** можно использовать для установки начального значения **атрибутов** экземпляра.


> Hint: In the example above, the **__init__** method takes two arguments and assigns them to the object's attributes. The **__init__** method is called the class constructor.

> Подсказка: в приведенном выше примере метод **__init__** принимает два аргумента и присваивает их атрибутам объекта. Метод **__init__** называется конструктором класса.

### Methods 

Classes can have other **methods** defined to add functionality to them. 
Remember, that all methods must have **self** as their first parameter.
These methods are accessed using the same **dot** syntax as attributes.


Классы могут иметь другие **методы**, определенные для добавления к ним функциональности.
Помните, что все методы должны иметь **self** в качестве первого параметра.
Доступ к этим методам осуществляется с использованием того же синтаксиса **точки**, что и для атрибутов.

***

## Inheritance

### Inheritance

**Inheritance** provides a way to share functionality between classes. 

Imagine several classes, **Cat, Dog, Rabbit** and so on. Although they may differ in some ways (only **Dog** might have the method **bark**), they are likely to be similar in others (all having the **attributes color** and **name**). 
This similarity can be expressed by making them all inherit from a **superclass Animal**, which contains the shared functionality. 
To **inherit** a class from another class, put the superclass name in parentheses after the class name.

**Наследование** обеспечивает возможность совместного использования функций между классами.

Представьте себе несколько классов: **Кошка, Собака, Кролик** и так далее. Хотя они могут отличаться в чем-то (только **Собака** может иметь метод **лай**), они, вероятно, будут похожи в других (все они имеют **атрибуты цвета** и **имя**). .
Это сходство может быть выражено в том, что все они наследуются от **суперкласса Animal**, который содержит общие функции.
Чтобы **наследовать** класс от другого класса, поместите имя суперкласса в круглые скобки после имени класса.

	class Animal: 
      def __init__(self, name, color):
        self.name = name
        self.color = color
    class Cat(Animal):
      def purr(self):
        print("Purr...")
        
    class Dog(Animal):
      def bark(self):
        print("Woof!")

    fido = Dog("Fido", "brown")
    print(fido.color)
    fido.bark()

### Inheritance 

A class that inherits from another class is called a **subclass**.
A class that is inherited from is called a **superclass**.
If a class inherits from another with the same attributes or methods, it overrides them.

Класс, который наследуется от другого класса, называется **подклассом**.
Класс, унаследованный от, называется **суперклассом**.
Если класс наследуется от другого с теми же атрибутами или методами, он переопределяет их.

    class Wolf: 
      def __init__(self, name, color):
        self.name = name
        self.color = color
  
      def bark(self):
         print("Grr...")
         
    class Dog(Wolf):
      def bark(self):
        print("Woof")
        
    husky = Dog("Max", "grey")
    husky.bark() 

> Hint: In the example above, Wolf is the superclass, Dog is the subclass.

> Подсказка: в приведенном выше примере Wolf — это надкласс, а Dog — подкласс.

### Inheritance 

The function super is a useful inheritance-related function that refers to the parent class. It can be used to find the method with a certain name in an object's **superclass**.

Функция super — полезная функция, связанная с наследованием, которая ссылается на родительский класс. Его можно использовать для поиска метода с определенным именем в **суперклассе** объекта.

    class A:
      def spam(self):
        print(1)
        
    class B(A):
      def spam(self):
        print(2)
        super().spam()
            
    B().spam()

> Hint: **super().spam()** calls the spam method of the **superclass**.

> Подсказка: **super().spam()** вызывает спам-метод **суперкласса**.

***

## Magic Methods & Operator Overloading

### Magic Methods

**Magic methods** are special methods which have **double underscores** at the beginning and end of their names. 

They are also known as **dunders**. 

So far, the only one we have encountered is **__init__**, but there are several others. 

They are used to create functionality that can't be represented as a normal method. 

One common use of them is **operator** overloading. 

This means defining operators for custom classes that allow operators such as + and * to be used on them.

An example magic method is **__add__** for +

**Магические методы** — это специальные методы, имена которых имеют **двойные символы подчеркивания** в начале и в конце.

Они также известны как **дандеры**.

Пока что мы столкнулись только с **__init__**, но есть и другие.

Они используются для создания функциональности, которую нельзя представить в виде обычного метода.

Одним из их распространенных применений является **перегрузка оператора**.

Это означает определение операторов для пользовательских классов, которые позволяют использовать в них такие операторы, как + и *.

Пример магического метода: **__add__** для + 

    class Vector2D:
      def __init__(self, x, y):
        self.x = x
        self.y = y
      def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
        
    first = Vector2D(5, 7)
    second = Vector2D(3, 9)
    result = first + second
    print(result.x)
    print(result.y)

> Hint: The **__add__** method allows for the definition of a custom behavior for the + operator in our class.
As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
Once it's defined, we can add two objects of the class together.

> Подсказка: метод **__add__** позволяет определить пользовательское поведение для оператора + в нашем классе.
Как видите, он добавляет соответствующие атрибуты объектов и возвращает новый объект, содержащий результат.
Как только он определен, мы можем добавить два объекта класса вместе.

### Magic Methods 


More magic methods for common operators:

Больше магических методов для стандартных операторов

* __sub__ for -

* __mul__ for *

* __truediv__ for /

* __floordiv__ for //

* __mod__ for %

* __pow__ for **

* __and__ for &

* __xor__ for ^

* __or__ for |

The expression x + y is translated into x.**__add__**(y). 

However, if x hasn't implemented **__add__**, and x and y are of different types, then y.**__radd__**(x) is called. 

There are equivalent r methods for all magic methods just mentioned.

Выражение x + y преобразуется в x.**__add__**(y).

Однако, если x не реализовал **__add__**, а x и y имеют разные типы, то вызывается y.**__radd__**(x).

Существуют эквивалентные r методов для всех только что упомянутых магических методов.

    class SpecialString:
      def __init__(self, cont):
        self.cont = cont
        
      def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
        
    spam = SpecialString("spam")
    hello = SpecialString("Hello world!")
    print(spam / hello)

> Hint: In the example above, we defined the division operation for our class SpecialString.

> Подсказка: в приведенном выше примере мы определили операцию деления для нашего класса SpecialString.


### Magic Methods for comparisons


Python also provides magic methods for comparisons.

Python так-же содержит магические методы для сравнения

* __lt__ for <

* __le__ for <=

* __eq__ for ==

* __ne__ for !=

* __gt__ for >

* __ge__ for >=

 If __ne__ is not implemented, it returns the opposite of __eq__. 
There are no other relationships between the other operators.

Если __ne__ не реализовано, возвращается значение, противоположное __eq__.
Других отношений между другими операторами нет.


    class SpecialString:
      def __init__(self, cont):
        self.cont = cont
        
      def __gt__(self, other):
        for index in range(len(other.cont)+1):
          result = other.cont[:index] + ">" + self.cont
          result += ">" + other.cont[index:]
          print(result)
          
    spam = SpecialString("spam")
    eggs = SpecialString("eggs")
    spam > eggs


> Hint: As you can see, you can define any custom behavior for the overloaded operators.

> Подсказка: Как видите, вы можете определить любое пользовательское поведение для перегруженных операторов.

### Magic Methods 

There are several magic methods for making classes act like containers.
Есть несколько магических методов что бы  заставить классы работать как контейнеры.

* __len__ for len()

* __getitem__ for indexing

* __setitem__ for assigning to indexed values

* __delitem__ for deleting indexed values

* __iter__ for iteration over objects (e.g., in for loops)

* __contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.

Есть много других магических методов, которые мы не будем здесь рассматривать, например __call__ для вызова объектов как функций, и __int__, __str__ и им подобных для преобразования объектов во встроенные типы.

    import random
    
    class VagueList:
      def __init__(self, cont):
        self.cont = cont
        
      def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]
        
      def __len__(self):
        return random.randint(0, len(self.cont)*2)
        
    vague_list = VagueList(["A", "B", "C", "D", "E"])
    print(len(vague_list))
    print(len(vague_list))
    print(vague_list[2])
    print(vague_list[2])

> Hint: We have overridden the len() function for the class VagueList to return a random number.
The indexing function also returns a random item in a range from the list, based on the expression.

> Подсказка: Мы переопределили функцию len() для класса VagueList, чтобы она возвращала случайное число.
Функция индексирования также возвращает случайный элемент в диапазоне из списка на основе выражения.

