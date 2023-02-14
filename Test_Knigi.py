from pandas import Series, DataFrame
import pandas as pd

numbers = Series([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
                  2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
                 index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

print(numbers.index)
print(numbers.values)
print(numbers % 8)

