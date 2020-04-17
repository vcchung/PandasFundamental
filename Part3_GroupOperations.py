import pandas as pd

data = {'book': ['book1', 'book2', 'book3', 'book4'], 'author': ['peter', 'mary', 'peter', 'mary'],
        'publishYear': [2001, 2009, 2020, 1998]}
df = pd.DataFrame(data)
groupby = df.groupby('author')

print(type(groupby))
# output
# <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

for name, group in groupby:
    print('group name:' + name)
    print(group)

# find the min max publish year in each group
for name, group in groupby:
    year_min = group['publishYear'].min()
    year_max = group['publishYear'].max()
    print("publish year for group {}: min {} max {}".format(name, year_min, year_max))

# fill NAN with most common element in the group
data = {'type': ['book', 'magazine', 'magazine', None, None, 'book', 'book', 'magazine'],
        'author': ['peter', 'peter', 'peter', 'peter', 'mary', 'mary', 'mary', 'mary']}
df = pd.DataFrame(data)
groupby = df.groupby('author')


def fill_values(series):
    value_counts = series.value_counts()
    if value_counts.empty:
        return series
    most_frequent = value_counts.index[0]
    mew_series = series.fillna(most_frequent)
    print(mew_series)
    return mew_series


grouped_df = []
for name, group in groupby:
    group.loc[:, 'type'] = fill_values(group['type'])
    grouped_df.append(group)

new_df = pd.concat(grouped_df)

# None still exist in original df
print(df)

# None is filled with most frequent elements in the group
print(new_df)

# Build in methods is better!

# transform
data = {'type': ['book', 'magazine', 'magazine', None, None, 'book', 'book', 'magazine'],
        'author': ['peter', 'peter', 'peter', 'peter', 'mary', 'mary', 'mary', 'mary'],
        'age': [1, 2, 3, 4, 5, 6, 7, 8]}
df = pd.DataFrame(data)

df_groupby = df.groupby('author')
df.loc[:, 'type'] = df_groupby['type'].transform(fill_values)
print(df)

# aggregation
age__min = df.groupby('author')['age'].min()
age__max = df.groupby('author')['age'].max()
print(age__min)
# output
# mary     5
# peter    1
print(age__max)
# output
# mary     8
# peter    4

# filter
df_groupby = df.groupby('author')
condition = lambda x: x['age'].max() > 5
groupby_filter = df_groupby.filter(condition)
print(groupby_filter)
# output
# only mary group exist
