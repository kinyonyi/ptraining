import pandas as pd

df = pd.read_excel("pokemon_data.xlsx")

#using the query string, supply a variable to it
max_hp = 30
max_attack = 50

print(df.query("HP > @max_hp and Attack > @max_attack")[['Name', 'Type 2']])

new_df = df.query("HP > @max_hp and Attack > @max_attack")[['Name', 'Type 2']]
print(new_df)

#get the mean, median, mode for Speed

#mean for a single column
meanValue = df['Attack'].mean()
print(meanValue)

#getting the mode
modeValue = df['Attack'].mode()[0]
print(modeValue)

#getting the median
medianValue = df['Attack'].median()
print(medianValue)

#get for me the maximum and minimum value for the Attack (indexes)
max_index_value = df['Attack'].idxmax()
min_index_value = df['Attack'].idxmin()

print(max_index_value)
print(min_index_value)

#getting the row where the maximum value is found
print(max_index_value)
print(df.iloc[max_index_value])

#getting the maximum and the minimum values 
max_value = df['Attack'].max()
min_value = df['Attack'].min()

print(max_value)
print(min_value)

#replace all values where Speed > 120 with the mean value for the Speed 
meanSpeed = df['Speed'].mean()
for x in df.index:
    print(df.loc[x, "Speed"])
    if df.loc[x, "Speed"] > 120:
        df.loc[x, "Speed"] = meanSpeed

#aggregations 
grouped1 = df[['Type 1', "Attack", "Speed"]].groupby("Type 1").mean()
print(grouped1)

grouped2 = df[["Type 1", "Type 2", "Attack", "Speed"]].groupby(["Type 1","Type 2"]).mean()
print(grouped2)

#list the first 5 highest speed values 
print(df['Speed'].nlargest(5))
print(df['Speed'].nsmallest(5))

largest = df['Speed'].nlargest(5).index
print(largest)

for x in largest:
    print(df.iloc[x])