import pandas as pd

#################################################
# Loading data into pandas (through a data frame)

# df is short for data frame
df = pd.read_csv('pokemon_data.csv') # load csv file

#print(df)

# print(df.head(3)) # loads the first 3 columns

# print(df.tail(3)) # loads the last 3 columns

# df_xlsx = pd.read_excel('pokemon_data.xlsx') # load xlsx file

# print(df_xlsx.head(3))

#df = pd.read_csv('pokemon_data.txt', delimiter = '\t')   # tabs are seperating the columns in txt file
#print(df)


###############################################
# Reading Data in Pandas

# Read Headers
print(df.columns)

# Read each column
#print(df['Name'])
#print(df['Name'][0:5]) # first 5 elements

# Reading multiple columns
#print(df[['Name', 'Type 1', 'HP']])

# Reach Each Row
#print(df.iloc[0:4]) # printing the first 4 rows - iloc stands for integer location
#print(df.iloc[5])
#print(df.loc[(df['Type 1'] == "Fire") | (df['Type 2'] == "Fire")]) # Allows me to print only the fire elements

# Read a specific location (Row, Column)
#print(df.iloc[2,1])

# Iterating through each row
"""
for index, row in df.iterrows():
    print(index, row)
"""

#############################################################
# Sorting/Describing Data
#print(df.describe()) # gives brief summary of metrics of the data

#print(df.sort_values('Name')) # sort alphabetically
#print(df.sort_values('Name', ascending = False)) # Sort by descending

#print(df.sort_values(['Type 1', 'HP'], ascending = [1,0])) # sorting Type 1 from A-Z and HP by highest to lowest

#############################################################
# Making changes to the data
# adding up all the columns in each row
#df['Total'] = df['HP'] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df['Sp. Def'] + df['Speed']
#print(df.head(5))
#df = df.drop(columns = ['Total']) # droppin the total column
#print(df.head(5))

# More efficient way to add data
df['Total'] = df.iloc[:, 4:10].sum(axis = 1) # :, just mean were using all the rows, 4:9 is saying were looking at the 4th column to the 9th column (goes up to tenth column but does not include it), sum(axis = 1) adds these columns horizontally
print(df.head(5))

# reformat the order of the columns
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))