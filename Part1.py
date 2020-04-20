import pandas as pd

data = {'name': ['peter', 'Marry', 'Rose'], 'age': [12, 15, 12], 'isBoy': [True, False, False]}
df = pd.DataFrame(data)

# Exercise 1
# selection of column or columns
# ---------------------------------------------------
print(df['name'])
# output
# 0    peter
# 1    Marry
# 2     Rose
# Name: name, dtype: object

print(df[['name', 'isBoy']])
# output
    # name  isBoy
# 0  peter   True
# 1  Marry  False
# 2   Rose  False

print(df[['name', 'isBoy']]['isBoy'])
# output
# 0     True
# 1    False
# 2    False
# Name: isBoy, dtype: bool

# not recommended way to select column
# print(df.name)

# Exercise 2
# Total number of distinct isBoy
# ---------------------------------------------------
print(pd.unique(df['isBoy']))
# output
# [ True False]

print(len(pd.unique(df['age'])))
# output
# 2

# Exercise 3
# Filtering
# ---------------------------------------------------
filtered = df['age'] == 12
print(filtered.value_counts())
# output
# True     2
# False    1
# Name: age, dtype: int64

print(df['isBoy'].value_counts())
# output
# False    2
# True     1
# Name: isBoy, dtype: int64

# Exercise 4
# Proper indexing loc and iloc
# ---------------------------------------------------
print(df.loc[:, :])
print(df.loc[1:2, 'isBoy'])
print(df.loc[1:2, ['isBoy', 'name']])
print(df.loc[df['age'] == 12, ['isBoy', 'name']])

print(df.iloc[:,:])
print(df.iloc[:, 0:2])
print(df.iloc[1, 0:2])
