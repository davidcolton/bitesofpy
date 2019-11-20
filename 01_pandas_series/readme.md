# Let's get started with Pandas. Introducing Pandas Series

In case you are not aware of who, or what, `pandas` is, [pandas](https://pandas.pydata.org/) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

The two primary data structures in `pandas` are the ***Series*** and the ***DataFrame***. The simplest way to visualise  these two structures is to use an analogy with your favourite Spreadsheet application. Think a a `pandas` Series as Column A, 1 dimension,  plus the row indexes. A Dataframe is the whole spreadsheet, 2 dimensions, with both rows and columns.

This is what a Series looks like in a Spreadsheet.

<img src="./series_spreadsheet.png" alt="image-20191120082100666" style="zoom:50%;" />

In a spreadsheet the row indexes typically start at `1` and the column names typically start at `A`. The Series called `A` above has four value `[1, 2, 3, 4]`.

This is what a similar Series looks like in `pandas`:

```>>> x
>>> x
0    1
1    2
2    3
Name: Fred, dtype: int64
```

The `pandas` Series Python variable is named `x`. The default index, like all other Python objects, are zero-based so the index values are `[0, 1, 2]`and the series values are `[1, 2, 3]`. The sample `x` series shown is called `Fred` and all the series values are of type `int64`.

## Creating Series

Now that you know everything that you need to know about `pandas` Series it's time for you to start creating some series of your own. In this Bite you are asked to complete a number of functions that each create a `pandas` Series. How you create each series is up to you but if you do your research you'll find that Series can be created from all different type of Python Objects:

1. Create a Series with values `[1, 2, 3, 4, 5]` of type `int64`, don't worry about the index but make the `Fred` the name of the Series
2. Create a Series with values `[0.000, 0.001, ... 0.999, 1.000]` of type `float64`, don't worry about the index
3. Create a Series with values `[1, 2, ... 25, 26]` of type `int64`, and add an index with values `[a, b, ... y, z]` so index `a = 1`, `b = 2` ... `y = 25`, `z = 26`
4. Create a Series with values `[A, B, ... Y, Z]` of type `object`, and add an index with values `[101, 102, ... 125, 126]` so index `101 = 'A'`, `102 = 'B'` ... `125 = 'Y'`, `126 = 'Z'`

## Accessing Series Elements

Now that you know how to create a Series you want to get specific elements from Series to potentially work on them in some manner. When accessing elements you have multiple option. You can access specific index locations, slices, `.loc`and `.iloc` functions. How you solve this next set of challenges in not the issue, returning the expected values is the requirement.

1. Return the value at the given index location
2. Return the slice of the Series given by the start and end slice positions
3. Return the slice of the Series given by the start and end positions inclusive
4. Return the first n elements in a Series
5. Return the last n elements in a Series
6. Return all indexes as a list
7. Return all values as a list

In the next `pandas` Bite Challenge we will look at more Series operations before moving onto Dataframes.

