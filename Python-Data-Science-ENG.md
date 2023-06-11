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

***

## More Statistic

### Standard Deviation


The **Standard Deviation** is a measure of how spread out our data is.
To calculate it, we first need to calculate a value called **Variance**: which is the average of the squared differences from the **mean**.

So, for our prices data:

	[14, 18, 19, 24, 26, 33, 42, 55, 67] 

The mean is **33.1**. To calculate the variance, we take the difference between each value and the mean, square it, and then average the result: Variance = **292.5**

Now we take the square root of the Variance, to get the Standard Deviation: std = 17.1

	import math
	
	list = [14, 18, 19, 24, 26, 33, 42, 55, 67]
	mean = round(sum(list) / len(list), 2)
	
	sum = 0
	
	for i in list:
	    sum += (i - mean)**2
	    
	sum /= len(list)
	print(round(math.sqrt(sum), 2)) # Variance is 17.10

Now, we can check which ages are within one standard deviation (17.1) from the mean (33.1) - from (33.1-17.1) to (33.1+17.1):


	[14, 18, 19, 24, 26, 33, 42, 55, 67]
	
	[18, 19, 24, 26, 33, 42]  
As you can see, 6 values out of 9 are within that range.

> Hint: A low standard deviation indicates that the values tend to be close to the mean of the set, while a high standard deviation indicates that the values are spread out over a wider range.

### Statistic

We have learned how to calculate the main summary statistics for a data set:
**mean**: the average of the values.
**median**: the middle value.
**standard deviation**: the measure of spread.

These statistics provide information about your data set and help you understand where your data values are and how they are distributed.

> Hint: Python provides libraries that calculate the summary statistics for you. We will learn about them in later lessons.
***

# Math Operations with NumPy

## What is NumPy

### NumPy

NumPy (Numerical Python) is a Python library used to work with numerical data.
NumPy includes functions and data structures that can perform a wide variety of mathematical operations.

To start using NumPy, we first need to import it:

	import numpy as np 

> Hint: np is the most common name used to import numpy.

### NumPy Array

In Python, lists are used to store data.
NumPy provides an array structure for performing operations with data.
NumPy arrays are faster and more compact than lists.

A NumPy array can be created using the np.array() function, providing it a list as the argument:

	x = np.array([1, 2, 3, 4]) 

Now, x is a NumPy array containing 4 values.
We can access its elements using their indexes, which start from 0:

	print(x[0]) # Output is 1

> Hint: NumPy arrays are homogeneous, meaning they can contain only a single data type, while lists can contain multiple different types of data.

*** 

## Using NumPy arrays

### NumPy Arrays

NumPy arrays are often called ndarrays, which stands for "N-dimensional array", because they can have multiple dimensions.

#### #### For example:

	x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	print(x[1][2])

This will create a 2-dimensional array, which has 3 columns and 3 rows, and output the value at the 2nd row and 3rd column.

Arrays have properties, which can be accessed using a dot.
ndim returns the number of dimensions of the array.
size returns the total number of elements of the array.
shape returns a tuple of integers that indicate the number of elements stored along each dimension of the array.

#### For example:

	x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
	print(x.ndim) # 2
	print(x.size) # 9
	print(x.shape) # (3, 3)

> Hint: So, the array in our example has 2 dimensions, 9 elements and is a 3x3 matrix (3 rows and 3 columns).


### NumPy Arrays

We can add, remove and sort an array using the np.append(), np.delete() and np.sort() functions.

#### For example:

	import numpy as np

	x = np.array([2, 1, 3])
	x = np.append(x, 4)
	x = np.sort(x)

	print(x) # Output is [1, 3, 4]

np.arange() allows you to create an array that contains a range of evenly spaced intervals (similar to a Python range):

	import numpy as np

	x = np.arange(2, 10, 3)
	print(x) #x is [2, 5, 8]

## Changing the Shape

### Reshape

Recall that shape refers to the number of rows and columns in the array.
For example, let's consider the following array:

	x = np.arange(1, 7)

This is a 1-dimensional array, containing 6 elements.

NumPy allows us to change the shape of our arrays using the reshape() function. For example, we can change our 1-dimensional array to an array with 3 rows and 2 columns:

	z = x.reshape(3, 2)

>Hint: When you use the reshape method, the array you want to produce needs to have the same number of elements as the original array.

### Reshape

Reshape can also do the opposite: take a 2-dimensional array and make a 1-dimensional array from it:

	x = np.array([[1, 2], [3, 4], [5, 6]])
	z = x.reshape(6)

The result is a flat array that contains 6 elements.

> Hint: The same result can be achieved using the flatten() function.

## Indexing and Slicing

### Indexing and Slicing

NumPy arrays can be indexed and sliced the same way that Python lists are.

	import numpy as np
		
	x = np.arange(1, 10)
		
	print(x[0:2])
	print(x[5:])
	print(x[:2])
	print(x[-3:])

> Hint: Negative indexes count from the end of the array, so, [-3:] will result in the last 3 elements.

### Conditions


You can provide a condition as the index to select the elements that fulfill the given condition.

For example, let's select the elements that are less than 4:

	import numpy as np
	
	x = np.arange(1, 10)
	
	print(x[x<4])

Conditions can be combined using the & (and) and | (or) operators.
For example, let's take the even numbers that are greater than 5:

> Hint: The condition can also be assigned to a variable, which will be an array of boolean values showing whether or not the values in the array fulfill the condition:
y = (x>5) & (x%2==0)

***

## Array Operations

### Operations

It is easy to perform basic mathematical operations with arrays.
For example, to find the sum of all elements, we use the sum() function:


	import numpy as np

	x = np.arange(1, 10)

	print(x.sum())

Similarly, min() and max() can be used to get the smallest and largest elements.

We can also perform operations between the array and a single number.
For example, we can multiply all elements by 2:

	import numpy as np

	x = np.arange(1, 10)
	y = x*2

	print(y)	

As simple as that! Take your array and perform any operation you want with it!

> Hint: NumPy understands that the given operation should be performed with each element. This is called broadcasting.

### Statistics

Remember the summary statistics we learned in the previous module? Those included **mean, median, variance** and **standard deviation**.

NumPy arrays have built-in functions to return those values.

	import numpy as np

	x = np.array([14, 18, 19, 24, 26, 33, 42, 55, 67])
	
	print(np.mean(x))
	print(np.median(x))
	print(np.var(x))
	print(np.std(x))


> Hint: As you can see, NumPy provides many useful functions to perform common operations with arrays.

***

# Data Manipulation with Pandas

## What is Pandas?

### What is Pandas?

Pandas is one of the most popular data science libraries in Python. Easy to use, it is built on top of NumPy and shares many functions and properties.

With Pandas, you can read and extract data from files, transform and analyze it, calculate statistics and correlations, and much more!

To start using pandas, we need to import it first:

	import pandas as pd 

pd is a common short name used when importing the library.

> Hint: Pandas is derived from the term "panel data", an econometrics term for data sets that include observations over multiple time periods for the same individuals.

### Series & DataFrames


The two primary components of pandas are the Series and the DataFrame.

A Series is essentially a column, and a DataFrame is a multi-dimensional table made up of a collection of Series.

For example, the following DataFrame is made of two Series, ages and heights

![Example](https://api.sololearn.com/DownloadFile?id=4554)

> Hint: You can think of a Series as a one-dimensional array, while a DataFrame is a multi-dimensional array.

***

## Creating DataFrames

### DataFrames

Before working with real data, let's first create a DataFrame manually to explore its functions.
The easiest way to create a DataFrame is using a dictionary:

	data = {
	   'ages': [14, 18, 24, 42],
	   'heights': [165, 180, 176, 184]
	}

Each key is a column, while the value is an array representing the data for that column.

Now, we can pass this dictionary to the DataFrame constructor:

	import pandas as pd

	data = {
	   'ages': [14, 18, 24, 42],
	   'heights': [165, 180, 176, 184]
	}
	
	df = pd.DataFrame(data)
	print(df)

### DataFrames 

The DataFrame automatically creates a numeric index for each row.
We can specify a custom index, when creating the DataFrame:

	import pandas as pd

	data = {
	   'ages': [14, 18, 24, 42],
	   'heights': [165, 180, 176, 184]
	}
	
	df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
	print(df)

Now we can access a row using its index and the loc[] function:

	import pandas as pd
	
	data = {
	   'ages': [14, 18, 24, 42],
	   'heights': [165, 180, 176, 184]
	}
	
	df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
	print(df.loc["Bob"])

This will output the row that corresponds to the index "Bob".

> Hint: Note, that loc uses square brackets to specify the index.

***

## Indexing & Slicing

### Indexing

We can select a single column by specifying its name in square brackets:

	import pandas as pd

	data = {
   	'ages': [14, 18, 24, 42],
 	  'heights': [165, 180, 176, 184]
	}
	
	df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
	
	print(df["ages"])

The result is a Series object.

If we want to select multiple columns, we can specify a list of column names:

	import pandas as pd

	data = {
 	  'ages': [14, 18, 24, 42],
 	  'heights': [165, 180, 176, 184]
	}

	df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])

	print(df[["ages", "heights"]])

This time, the result is a DataFrame, as it includes multiple columns.

> Hint: This is useful, when we need to select only a part of the columns from the dataset.

### Slicing

Pandas uses the iloc function to select data based on its numeric index.
It works the same way indexing lists does in Python.

	import pandas as pd
	
	data = {
 	  'ages': [14, 18, 24, 42],
 	  'heights': [165, 180, 176, 184]
	}

	df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])

	# third row
	print(df.iloc[2])
	
	#first 3 rows
	print(df.iloc[:3])
	
	# rows 2 to 3
	print(df.iloc[1:3])

> Hint: iloc follows the same rules as slicing does with Python lists.

### Conditions

We can also select the data based on a condition.
For example, let's select all rows where age is greater than 18 and height is greater than 180:

	import pandas as pd
		
	data = {
 	  'ages': [14, 18, 24, 42],
 	  'heights': [165, 180, 176, 184]
	}
		
	df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
		
	print(df[(df['ages']>18) & (df['heights']>180)])

> Hint: Similarly, the or | operator can be used to combine conditions.
***

## Reading Data

### Reading Data


It is quite common for data to come in a file format. One of the most popular formats is the CSV (comma-separated values).
Pandas supports reading data from a CSV file directly into a DataFrame.

For our examples, we will use a CSV file that contains the COVID-19 infection data in California for the year 2020, called 'ca-covid.csv'.

The read_csv() function reads the data of a CSV file into a DataFrame:

	df = pd.read_csv("ca-covid.csv")

We need to provide the file path to the read_csv() function.

> Hint: Pandas also supports reading from JSON files, as well as SQL databases.

### Reading Data

Once we have the data in a DataFrame, we can start exploring it.
We can get the first rows of the data using the head() function of the DataFrame:

	import pandas as pd
	
	df = pd.read_csv("/uploads/ca-covid.csv")
	
	print(df.head()) 

![Example](https://api.sololearn.com/DownloadFile?id=4558)

By default it returns the first 5 rows. You can instruct it to return the number of rows you would like as an argument (for example, df.head(10) will return the first 10 rows).

We can see that our DataFrame contains the date, state, number of cases and deaths for that date.

> Hint: Similarly, you can get the last rows using the tail() function.

### Reading Data


The info() function is used to get essential information about your dataset, such as number of rows, columns, data types, etc:

	import pandas as pd

	df = pd.read_csv("uploads/ca-covid.csv")

	df.info()

From the result, we can see that our dataset contains 342 rows and 4 columns: date, state, cases, deaths.

We also see that Pandas has added an auto generated index.
We can set our own index column by using the set_index() function:


	import pandas as pd

	df = pd.read_csv("uploads/ca-covid.csv")
	df.set_index("date", inplace=True)

	print(df.head())	

The date column is a good choice for our index, as there is one row for each date.


> Hint: The inplace=True argument specifies that the change will be applied to our DataFrame, without the need to assign it to a new DataFrame variable.

### Dropping a Column


Since our data is only for the state of California, we can remove that column from our DataFrame, as it contains the same value for all rows:

	import pandas as pd
	
	df = pd.read_csv("uploads/ca-covid.csv")
	df.set_index('date', inplace=True)
	df.drop('state', axis=1, inplace=True)
	
	df.info()

* drop() deletes rows and columns.
* axis=1 specifies that we want to drop a column.
* axis=0 will drop a row.

> Hint: Now our dataset is much cleaner: we have a date index, and casesdeaths columns.

	
