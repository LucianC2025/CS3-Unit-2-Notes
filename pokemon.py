import numpy as np
import pandas as pd

# Load CSV file data into DataFrame
pokemon = pd.read_csv('pokemon_data.csv')

print("**** Pokemon DataFrame ****")
print(pokemon) # Prints the first 5 rows and the last 5 rows 

print()

print("**** Pokemon Columns ****")
print(pokemon.columns) # See Column labels. Returns a List of Strings that represents the column names

print()

# Acess one column (Series) of data
print("** Acessesing Type 1 Column **")
print(pokemon['Type 1'])

print()

# Shorthand way of referencing a column
print("** Acessesing HP Column **")
print(pokemon.HP)

print()

# Create new column for Attack/Sp. Atk ratio
pokemon['Attack Ratio'] = pokemon['Attack'] / pokemon['Sp. Atk']
print('** Attack Ratio **')
print(pokemon['Attack Ratio'])







print()

# You can replace the standard indicies (0...end) with strings from one column!
poke = pokemon.set_index('Name') 

# Access a specific "cell" (ROW, COL)
print("Pickachu's type:", poke.loc['Pikachu', 'Type 1'])

print()

# Acess a range of ROWS
print("Acessing a range of rows..")
print(poke.loc[['Bulbasaur', 'Squirtle', 'Charmander']])

print()

# If you want to print every row in a certain way
for index, row in poke.iterrows():
    print(index, "-", row['Type 1'])