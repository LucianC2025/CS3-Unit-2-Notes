# importing librariers "as" aliases
import numpy as np
import pandas as pd

# *** Pandas' SERIES object ***
# Series are 1D arrays of indexed data 
# Create Series from a list/array
data = pd.Series([0.24, 0.5, 0.75, 1.0]) # calling the SERIES constructor

print(data.values) # looks like a list, dropps any trailing zeros
print(data.index) # Prints a RangeIndex, range computed for indices

print()

# Acess series data by index
print("Getting one value from Series: ", data[1]) # Prints the index first and then the value
print("Getting multiple values will also show indices:")
# data[start_index:stop_index]
print(data[0:3]) # Not including stop index, in this case (3)
# If the values are not all the same data type the dtype is object

print()

# Series are like arrays but with EXPLICIT indexing
print("Assigning Explicit indexing....")
grades = pd.Series([9, 10, 11, 12],
                 index=['Freshman', 'Sophmore', 'Junior', 'Senior'])
print(grades)
# Acess Series data by index
print("Seniors are in", grades['Senior'], "grade")

print()

print("Creating a Series from a dictionary...")
# Can also create a Series from a dictionary
cookies_dict = {'double chocolate': 5,
                'chocolate chip': 10,
                'oatmeal raisin': 9,
                'snickerdoodle': 10,
                'dirt': 1 }
cookies = pd.Series(cookies_dict)
print(cookies) # keys become indecies of the Series
# Acess items by index
print("Rating of dirt cookies: ", cookies['dirt'])