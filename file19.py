#pip3 freeze > requirements.txt
#pip install -r requirements.txt

import pandas as pd

names = ["dave","mercy","isaac"]
pd_series = pd.Series(names,  name="names")
print(pd_series)
print(pd_series[2])
pd_series = pd.Series(names, index=["name1","name2","name3"],  name="names")
print(pd_series)
#operations an be performed
series = pd.Series([1,2,3,4,5])
result = series * 3
print(result)
#filters can be performed
result = result[result > 6]
print(result)
data = {
    "name":"david",
    "location":"kampala",
    "age":29
}
result = pd.Series(data, name="david's info")
print(result)
print(result.index)
print(result.values)
#specifying datra to be used for the series creation
result = pd.Series(data, index= ["name","age"], name="david's info")
print(result)
#mapping
data = pd.Series(["banana","charger","table"])
mapping = {"banana":"fruit", "charger":"electronic device","table":"furniture"}
mapped = data.map(mapping)
print(mapped)
data = pd.Series([1,2,3,4,4,3,5,6,8,3,2,1,7,None])
print(data.describe())
print(data.mean())
print(data.std())
print(data.mean())
print(data.sum())
print(data.head(3))
print(data.tail(3))
print(data.value_counts())
print(data.unique())
print(data.isnull())
print(data.isna())
print(data.sort_values())#default ascending order, ascending = False
print(data.sort_index())#sorting by index
#getting the maximum value 
print(data.idxmax())
#getting the minimum mum 
print(data.idxmin())
#getting the first n small numbers
print("n smallest")
print(data.nsmallest(4))
print("n largest")
print(data.nlargest(4))
print(data.apply(lambda x: (x * 2) - 2))
print(data.replace({8:5}))
print(data.isin([2,5,20,100]))
print(data.diff())
print(data.div(3))
print(data.pct_change())
print(data.cumsum())
print(data.cumprod())
print(data.cummin())
print(data.cummax())
print(data.clip(lower=3, upper=8))
print(data.add_prefix("index_"))
print(data.add_suffix("_index"))
print(data.between(5, 20))

data1 = pd.Series([1,2,3,4])
data2 = pd.Series([2,4,3,2])
print(data1.div(data2))
print(data1.divmod(data2))
print(data1.combine(data2, lambda x, y: x + y))
joined = pd.concat([data1, data2])
print(joined)
series = pd.Series([False, True, False, True, True])
print(series.any())#check whther any item in the list is true
print(series.all())
data1 = pd.Series([1,2,2,4,2,1,5])
print(data1.drop_duplicates())
data1 = pd.Series([1,2,None,2,4,2, None,1,5])
print(data.dropna())
print(data1.bfill())
data1 = pd.Series([1,2,2,4], index =["a","b","c","d"])
print(data1.loc['b'])
print(data1.loc['d'])
print(data1.loc['b':'d'])#specifying the range

data1 = pd.Series([1,2,2,4,2,1,5])
print(data1.loc[1])
print(data1.loc[3])
print(data1.loc[1:3])#specifying the range






