import pandas as pd

data = {'width': ['2', '13', 'peter', '20', '10', 'NAN'], 'height': ['rose', '20', 'NAN', '10', '50', '70']}
df = pd.DataFrame(data)

# find the top five to last five in the sorted list
print(df['width'].sort_values().head())
print(df['width'].sort_values().tail())

# coerce on errors will convert other values to NAN
print(pd.to_numeric(df['width'], errors='coerce'))
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')
print(df.loc[:, 'width'])
print(df.loc[:, 'height'])

area = df.loc[:, 'width'] * df.loc[:, 'height']
print(area.value_counts())

# add new column in DataFrame
df = df.assign(area=area)
print(df['area'])

# find the max or max record id in the Series
print(df['area'].max())
print(df['area'].idxmax())

print(df.loc[df['area'].idxmax(), :])
