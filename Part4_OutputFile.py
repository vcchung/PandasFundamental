import pandas as pd
import os

data = {'type': ['book', 'magazine', 'magazine', None, None, 'book', 'book', 'magazine'],
        'author': ['peter', 'peter', 'peter', 'peter', 'mary', 'mary', 'mary', 'mary'],
        'age': [1, 2, 3, 4, 5, 6, 7, 8]}
df = pd.DataFrame(data)

# Read and write pickle file
pd.to_pickle(df, os.path.join('.', 'data_frame.pickle'))

read_pickle = pd.read_pickle(os.path.join('.', 'data_frame.pickle'))
print(read_pickle)
# output
#  type author  age
# 0      book  peter    1
# 1  magazine  peter    2
# 2  magazine  peter    3
# 3      None  peter    4
# 4      None   mary    5
# 5      book   mary    6
# 6      book   mary    7
# 7  magazine   mary    8


# write to excel file
new_df = df.loc[2:5, :].copy()
print(new_df)
# output
# type author  age
# 2  magazine  peter    3
# 3      None  peter    4
# 4      None   mary    5
# 5      book   mary    6

# write file with index
new_df.to_excel('data_frame.xlsx')

# write file without index
new_df.to_excel('data_frame_without_index.xlsx', index=False)
