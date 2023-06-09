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

