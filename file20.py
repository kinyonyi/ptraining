#Dataframes
import pandas as pd

df = pd.read_excel("pokemon_data.xlsx")

#getting information about the dataframe 
print(df.info())

#gettng quick statistics about the dataframe 
print(df.describe())

#getting the column names 
print(df.columns)

#head and tail - default is 5, pass parameter to method with no of heads
print(df.head())
print(df.tail())

print(list(df.columns))

print(df['Name'])
columns_needed = ['Name','Type 2', 'Generation']
print(df[columns_needed])
#print(df[columns_needed].to_string())
print("These are the columns and rows")
print(df.iloc[[0,2,3]])

"""
data = {
    "marks":[20, 30, 40],
    "percentage":[10, 40, 60]
}

df = pd.DataFrame(data, index = ["m","n","o"])
print(df)
print(df.loc[["m","o"]])
"""

print(df.iloc[[0,2,3],[1,3,10]])
print(df.loc[[0,2,3],['Name','Type 2', 'Generation']])

#accessing a cell
print(df.iloc[0,2])
print(df.loc[0,'Name'])

print(df.query("HP > 30 and Attack > 50"))

print(df['Name'].str.contains("Dian"))
print(df[df['Name'].str.contains("Dian")])
print(df[df['Name'].str.lower().str.contains("Dian".lower())])

#sorting values 
print(df.sort_values("Name"))
print(df.sort_values("Name", ascending=False))

#sorting multiple columns
print(df.sort_values(by = ["Speed", "Name"], ascending=[True, False]).head(10))
print(df.sort_values(by = ["Speed"], ascending=[True]).head(10))

#food for thought
#Speed > 40 and (Type 1 = Buf or Type 2 = Poison)
#to display Name, Generation and attack values
#write this to a new excel file