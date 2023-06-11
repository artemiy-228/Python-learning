# Introduction / Вступление

## Statistic / Статистика

### Mean / Среднее арифметическое
Data Science uses various techniques and methods to extract knowledge and insights from data.
Let's dive into some basics of statistics first. These concepts form the main building blocks of data analysis.
As an example dataset, let's consider the prices of a group of products:

Наука о данных использует различные методы и методы для извлечения знаний и идей из данных.
Давайте сначала погрузимся в некоторые основы статистики. Эти концепции составляют основные строительные блоки анализа данных.
В качестве примера набора данных рассмотрим цены на группу товаров:


	[18, 24, 67, 55, 42, 14, 19, 26, 33]

The given dataset includes prices of 9 products.
Данный набор данных включает цены на 9 товаров.

The **mean** is the average value of the dataset. We can calculate it by adding all prices together and dividing by the number of products: 

**Среднее** – это среднее значение набора данных. Мы можем рассчитать его, сложив все цены вместе и разделив на количество продуктов:

	mean = 298/9 = 33.1

> Hint: Notice that the mean value is usually not part of our dataset.

> Подсказка: обратите внимание, что среднее значение обычно не является частью нашего набора данных.
### Median / Медиана(центральные значение)

Another useful concept is **median**: the middle value of an ordered dataset.
To calculate the median for our prices dataset, let's first order it in ascending order:

Еще одна полезная концепция — **медиана**: среднее значение упорядоченного набора данных.
Чтобы вычислить медиану для нашего набора данных о ценах, давайте сначала упорядочим его в порядке возрастания:

	[14, 18, 19, 24, 26, 33, 42, 55, 67]

	median = 26
The **median** is **26**, as that's the middle value.
If our dataset had an even number of values, we would take the two values in the middle and calculate their average value.

**Медиана** составляет **26**, так как это среднее значение.
Если бы в нашем наборе данных было четное количество значений, мы бы взяли два значения посередине и вычислили их среднее значение.

	[14, 18, 19, 24, 26, 25, 33, 42, 55, 67]

	median = 25.5

The median is generally more useful than the mean. This is because the mean can vary widely due to one value that is a lot larger or smaller than the others.


Медиана, как правило, более полезна, чем среднее значение. Это связано с тем, что среднее значение может сильно различаться из-за того, что одно значение намного больше или меньше других.

> Hint: The **mean** and the **median** are called
**Measures of Central Tendency**, as they describe where the center of our data is.

> Подсказка: **среднее** и **медиана** называются
**Показатели центральной тенденции**, так как они описывают, где находится центр наших данных.

***

## More Statistic / Больше статистики

### Standard Deviation / Среднеквадратичное отклонение


The **Standard Deviation** is a measure of how spread out our data is.
To calculate it, we first need to calculate a value called **Variance**: which is the average of the squared differences from the **mean**.

So, for our prices data:

**Среднеквадратичное отклонение** — это показатель того, насколько разбросаны наши данные.
Чтобы вычислить его, нам сначала нужно вычислить значение, называемое **Дисперсия**: среднее квадратов различий от **среднего**.

Итак, для наших ценовых данных:

	[14, 18, 19, 24, 26, 33, 42, 55, 67] 

The mean is **33.1**. To calculate the variance, we take the difference between each value and the mean, square it, and then average the result: Variance = **292.5**

Среднее значение составляет **33,1**. Чтобы вычислить дисперсию, мы берем разницу между каждым значением и средним значением, возводим ее в квадрат, а затем усредняем результат: Дисперсия = **292,5**

Now we take the square root of the Variance, to get the Standard Deviation: std = 17.1

Теперь мы возьмем квадратный корень из дисперсии, чтобы получить стандартное отклонение: стандартное отклонение = 17,1

	import math
	
	list = [14, 18, 19, 24, 26, 33, 42, 55, 67]
	mean = round(sum(list) / len(list), 2)
	
	sum = 0
	
	for i in list:
	    sum += (i - mean)**2
	    
	sum /= len(list)
	print(round(math.sqrt(sum), 2)) # Variance is 17.10

Now, we can check which ages are within one standard deviation (17.1) from the mean (33.1) - from (33.1-17.1) to (33.1+17.1):

Теперь мы можем проверить, какие возрасты находятся в пределах одного стандартного отклонения (17,1) от среднего (33,1) - от (33,1-17,1) до (33,1+17,1):

	[14, 18, 19, 24, 26, 33, 42, 55, 67]
	
	[18, 19, 24, 26, 33, 42]  
As you can see, 6 values out of 9 are within that range.

Как видите, 6 значений из 9 находятся в этом диапазоне.

> Hint: A low standard deviation indicates that the values tend to be close to the mean of the set, while a high standard deviation indicates that the values are spread out over a wider range.

> Совет. Низкое стандартное отклонение указывает на то, что значения, как правило, близки к среднему значению набора, а высокое стандартное отклонение указывает на то, что значения разбросаны по более широкому диапазону.

### Statistic / Статистика

We have learned how to calculate the main summary statistics for a data set:
**mean**: the average of the values.
**median**: the middle value.
**standard deviation**: the measure of spread.

These statistics provide information about your data set and help you understand where your data values are and how they are distributed.

Мы научились рассчитывать основную сводную статистику по набору данных:
**среднее**: среднее значение.
**медиана**: среднее значение.
**стандартное отклонение**: мера разброса.

Эти статистические данные предоставляют информацию о вашем наборе данных и помогают понять, где находятся значения ваших данных и как они распределяются.

> Hint: Python provides libraries that calculate the summary statistics for you. We will learn about them in later lessons.

> Подсказка: Python предоставляет библиотеки, которые вычисляют для вас сводную статистику. О них мы узнаем на следующих уроках.

***

# Math Operations with NumPy / Математические операции с NumPy

## What is NumPy / Что такое NumPy

### NumPy / NumPy

NumPy (Numerical Python) is a Python library used to work with numerical data.
NumPy includes functions and data structures that can perform a wide variety of mathematical operations.

To start using NumPy, we first need to import it:

NumPy (Numerical Python) — это библиотека Python, используемая для работы с числовыми данными.
NumPy включает в себя функции и структуры данных, которые могут выполнять широкий спектр математических операций.

Чтобы начать использовать NumPy, нам сначала нужно его импортировать:

	import numpy as np 

> Hint: np is the most common name used to import numpy.

> Подсказка: np — наиболее распространенное имя, используемое для импорта numpy.

### NumPy Array / NumPy Массивы

In Python, lists are used to store data.
NumPy provides an array structure for performing operations with data.
NumPy arrays are faster and more compact than lists.

A NumPy array can be created using the np.array() function, providing it a list as the argument:

В Python списки используются для хранения данных.
NumPy предоставляет структуру массива для выполнения операций с данными.
Массивы NumPy быстрее и компактнее списков.

Массив NumPy можно создать с помощью функции np.array(), предоставив ей список в качестве аргумента:

	x = np.array([1, 2, 3, 4]) 

Now, x is a NumPy array containing 4 values.
We can access its elements using their indexes, which start from 0:

Теперь x — это массив NumPy, содержащий 4 значения.
Мы можем получить доступ к его элементам, используя их индексы, которые начинаются с 0:

	print(x[0]) # Output is 1

> Hint: NumPy arrays are homogeneous, meaning they can contain only a single data type, while lists can contain multiple different types of data.

> Подсказка. Массивы NumPy однородны, то есть могут содержать данные только одного типа, тогда как списки могут содержать несколько разных типов данных.

*** 

## Using NumPy arrays/ Использование NumPy массивов

### NumPy Arrays/ NumPy массивы

NumPy arrays are often called ndarrays, which stands for "N-dimensional array", because they can have multiple dimensions.

#### #### For example:

Массивы NumPy часто называют ndarrays, что означает «N-мерный массив», поскольку они могут иметь несколько измерений.

#### #### Например:

	x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	print(x[1][2])

This will create a 2-dimensional array, which has 3 columns and 3 rows, and output the value at the 2nd row and 3rd column.

Это создаст двумерный массив, который имеет 3 столбца и 3 строки, и выведет значение во 2-й строке и 3-м столбце.

Arrays have properties, which can be accessed using a dot.
ndim returns the number of dimensions of the array.
size returns the total number of elements of the array.
shape returns a tuple of integers that indicate the number of elements stored along each dimension of the array.

#### For example:

Массивы имеют свойства, доступ к которым можно получить с помощью точки.
ndim возвращает количество измерений массива.
size возвращает общее количество элементов массива.
shape возвращает кортеж целых чисел, указывающих количество элементов, хранящихся в каждом измерении массива.

#### Например:

	x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
	print(x.ndim) # 2
	print(x.size) # 9
	print(x.shape) # (3, 3)

> Hint: So, the array in our example has 2 dimensions, 9 elements and is a 3x3 matrix (3 rows and 3 columns).

> Подсказка: Итак, массив в нашем примере имеет 2 измерения, 9 элементов и представляет собой матрицу 3x3 (3 строки и 3 столбца).


### NumPy Arrays/ NumPy массивы

We can add, remove and sort an array using the np.append(), np.delete() and np.sort() functions.

#### For example:

Мы можем добавлять, удалять и сортировать массив с помощью функций np.append(), np.delete() и np.sort().

#### Например:

	import numpy as np

	x = np.array([2, 1, 3])
	x = np.append(x, 4)
	x = np.sort(x)

	print(x) # Output is [1, 3, 4]

np.arange() allows you to create an array that contains a range of evenly spaced intervals (similar to a Python range):

np.arange() позволяет создать массив, содержащий диапазон равномерно расположенных интервалов (аналогично диапазону Python):

	import numpy as np

	x = np.arange(2, 10, 3)
	print(x) #x is [2, 5, 8]

## Changing the Shape / Изменение формы

### Reshape / Изменение

Recall that shape refers to the number of rows and columns in the array.
For example, let's consider the following array:

Напомним, что shape относится к количеству строк и столбцов в массиве.
Например, рассмотрим следующий массив:

	x = np.arange(1, 7)

This is a 1-dimensional array, containing 6 elements.

NumPy allows us to change the shape of our arrays using the reshape() function. For example, we can change our 1-dimensional array to an array with 3 rows and 2 columns:


Это одномерный массив, содержащий 6 элементов.

NumPy позволяет нам изменять форму наших массивов с помощью функции reshape(). Например, мы можем изменить наш одномерный массив на массив с 3 строками и 2 столбцами:

	z = x.reshape(3, 2)

>Hint: When you use the reshape method, the array you want to produce needs to have the same number of elements as the original array.

>Подсказка: когда вы используете метод изменения формы, массив, который вы хотите создать, должен иметь то же количество элементов, что и исходный массив.

### Reshape

Reshape can also do the opposite: take a 2-dimensional array and make a 1-dimensional array from it:

Reshape также может сделать обратное: взять 2-мерный массив и сделать из него 1-мерный массив:

	x = np.array([[1, 2], [3, 4], [5, 6]])
	z = x.reshape(6)

The result is a flat array that contains 6 elements.

В результате получается плоский массив, содержащий 6 элементов.

> Hint: The same result can be achieved using the flatten() function.
> Подсказка: Того же результата можно добиться с помощью функции flatten().

## Indexing and Slicing

### Indexing and Slicing

NumPy arrays can be indexed and sliced the same way that Python lists are.

Массивы NumPy можно индексировать и нарезать так же, как списки Python.

	import numpy as np
		
	x = np.arange(1, 10)
		
	print(x[0:2])
	print(x[5:])
	print(x[:2])
	print(x[-3:])

> Hint: Negative indexes count from the end of the array, so, [-3:] will result in the last 3 elements.

> Подсказка: Отрицательные индексы считаются с конца массива, поэтому [-3:] приведет к последним 3 элементам.

### Conditions


You can provide a condition as the index to select the elements that fulfill the given condition.

For example, let's select the elements that are less than 4:

Вы можете указать условие в качестве индекса для выбора элементов, которые удовлетворяют заданному условию.

Например, давайте выберем элементы меньше 4:

	import numpy as np
	
	x = np.arange(1, 10)
	
	print(x[x<4])

Conditions can be combined using the & (and) and | (or) operators.
For example, let's take the even numbers that are greater than 5:

Условия можно комбинировать с помощью знаков & (и) и | (или) операторы.
Например, возьмем четные числа больше 5:

> Hint: The condition can also be assigned to a variable, which will be an array of boolean values showing whether or not the values in the array fulfill the condition:
y = (x>5) & (x%2==0)

> Подсказка: Условие также может быть присвоено переменной, которая будет массивом логических значений, показывающих, удовлетворяют ли значения в массиве условию:
у = (х> 5) и (х% 2 == 0)

