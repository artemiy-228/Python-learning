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


