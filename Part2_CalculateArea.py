import pandas as pd

data = {'width': ['2', '13', 'peter', '20', '10', 'NAN'], 'height': ['rose', '20', 'NAN', '10', '50', '70']}
df = pd.DataFrame(data)

# find the top five to last five in the sorted list
print(df['width'].sort_values().head())
# output
# 4     10
# 1     13
# 0      2
# 3     20
# 5    NAN
# Name: width, dtype: object

print(df['width'].sort_values().tail())
# output
# 1       13
# 0        2
# 3       20
# 5      NAN
# 2    peter
# Name: width, dtype: object

# coerce on errors will convert other values to NAN
print(pd.to_numeric(df['width'], errors='coerce'))
# output
# 0     2.0
# 1    13.0
# 2     NaN
# 3    20.0
# 4    10.0
# 5     NaN
# Name: width, dtype: float64

df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

area = df.loc[:, 'width'] * df.loc[:, 'height']
print(area.value_counts())
# output
# 500.0    1
# 200.0    1
# 260.0    1
# dtype: int64

# add new column in DataFrame
df = df.assign(area=area)
print(df['area'])
# output
# 0      NaN
# 1    260.0
# 2      NaN
# 3    200.0
# 4    500.0
# 5      NaN
# Name: area, dtype: float64

# find the max or max record id in the Series
print(df['area'].max())
# output
# 500.0

print(df['area'].idxmax())
# output
# 4

print(df.loc[df['area'].idxmax(), :])
# output
# 4
# width      10.0
# height     50.0
# area      500.0
# Name: 4, dtype: float64