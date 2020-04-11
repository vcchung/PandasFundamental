import pandas as pd

data = {'name': ['peter', 'Marry', 'Rose'], 'age': [12, 15, 12], 'isBoy': [True, False, False]}
df = pd.DataFrame(data)

# Exercise 1
# selection of column or columns
# ---------------------------------------------------
# print(df['name'])
# print(df[['name', 'isBoy']]['isBoy'])

# not recommended
# print(df.name)

# Exercise 2
# Total number of distinct isBoy
# ---------------------------------------------------
# print(pd.unique(df['isBoy']))
# print(len(pd.unique(df['age'])))


# Exercise 3
# Filtering
# ---------------------------------------------------
# filtered = df['age'] == 12
# print(filtered.value_counts())
# print(df['isBoy'].value_counts())

# Exercise 4
# Proper indexing loc and iloc
# ---------------------------------------------------
# print(df.loc[:, :])
# print(df.loc[1:2, 'isBoy'])
# print(df.loc[1:2, ['isBoy', 'name']])
# print(df.loc[df['age'] == 12, ['isBoy', 'name']])

# print(df.iloc[:,:])
# print(df.iloc[:, 0:2])
# print(df.iloc[1, 0:2])
