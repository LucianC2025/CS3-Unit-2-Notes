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
# Series are 1D array with Labels, like columns
print("Assigning Explicit indexing....")
grades = pd.Series([9, 10, 11, 12],
                 index=['Freshman', 'Sophmore', 'Junior', 'Senior'])
print(grades)
# Acess Series data by index
print("Seniors are in", grades['Senior'], "grade")

print()

print("***************************** COOKIE RATINGS *****************************")
print("****************************Series ****************************")
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

print()
print("**************************** DataFrame ****************************")
print("Creating a DataFrame from a dictionary...")
# DataFrame is like a 2D array or specialized dictionary
cookies_df = pd.DataFrame(cookies, columns = ['rating'])
print(cookies_df)

print()

print("Adding a column to the DataFrame...")
# Add a column to our DataFrame
cookies_df['allergens'] = [True, True, True, True, False]
print(cookies_df)

print()

print("Another way to add a column...")
# Another way to add a column
cookies_df['sweetness'] = {'double chocolate': 10,
                'chocolate chip': 8,
                'oatmeal raisin': 5,
                'snickerdoodle': 7, 
                'dirt': -1,
                'birthday cake': 11} # if you give a key that doesn't exists in a column that doesn't exist doesn't work --> it isn't added
# Note: NaN means "Not a number"
print(cookies_df)

print()

print("***************************** DATA SELECTION *****************************")
print("Experimental Data 1...")
data = pd.Series(['l','u','c','i','a','n'], index = [1, 3, 5, 7, 9, 11])

# Indexing uses the explicit Index (the one we typed
print(data[3])

# Slicing (getting multiple values) uses IMPLICIT index (the excpected index: 0,1,2,3,4,....)
print(data[3:5])

print()
print("Experimental Data 2...")
n_data = pd.Series(['a', 'c', 'e'], index=[1,3,5])
print(n_data[3:5]) # Not getting excepted output

# Instead, use the LOC attribute to get a slice that uses explicit indicies
print("LOC...")
print(n_data.loc[3:5]) # Includes item at index 5 too!

print("iLoc...")
# Not as common, iLOC uses implicit indicies 
print(n_data.iloc[0:1]) # dosen't include second item