# Introduction

## Statistic

### Mean
Data Science uses various techniques and methods to extract knowledge and insights from data.
Let's dive into some basics of statistics first. These concepts form the main building blocks of data analysis.
As an example dataset, let's consider the prices of a group of products:

	[18, 24, 67, 55, 42, 14, 19, 26, 33]

The given dataset includes prices of 9 products.

The **mean** is the average value of the dataset. We can calculate it by adding all prices together and dividing by the number of products: 

	mean = 298/9 = 33.1

> Hint: Notice that the mean value is usually not part of our dataset.

### Median

Another useful concept is **median**: the middle value of an ordered dataset.
To calculate the median for our prices dataset, let's first order it in ascending order:

	[14, 18, 19, 24, 26, 33, 42, 55, 67]

	median = 26
The **median** is **26**, as that's the middle value.

If our dataset had an even number of values, we would take the two values in the middle and calculate their average value.

	[14, 18, 19, 24, 26, 25, 33, 42, 55, 67]

	median = 25.5

The median is generally more useful than the mean. This is because the mean can vary widely due to one value that is a lot larger or smaller than the others.

> Hint: The **mean** and the **median** are called
**Measures of Central Tendency**, as they describe where the center of our data is.
>> Measures of Central Tendency - Показатели центральной тенденции

