import pandas as pd
import os
import sqlite3

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

# write file with filtered columns
new_df.to_excel('data_frame_with_filtered_columns.xlsx', index=False, columns=['type', 'author'])

# multiple worksheets
excel_writer = pd.ExcelWriter('multiple_worksheets.xlsx')
df.to_excel(excel_writer, sheet_name='original_df', index=False)
new_df.to_excel(excel_writer, sheet_name='new_df', index=False)
excel_writer.save()


# Write to SQL table
with sqlite3.connect('myDb') as conn:
    new_df.to_sql('MyTable', conn)

# Write to JSON
print(new_df.to_json())
# output
# {"type":{"2":"magazine","3":null,"4":null,"5":"book"},"author":{"2":"peter","3":"peter","4":"mary","5":"mary"},"age":{"2":3,"3":4,"4":5,"5":6}}

print(new_df.to_json(orient='table'))
# output
# {"schema":{"fields":[{"name":"index","type":"integer"},{"name":"type","type":"string"},{"name":"author","type":"string"},{"name":"age","type":"integer"}],"primaryKey":["index"],"pandas_version":"0.20.0"},"data":[{"index":2,"type":"magazine","author":"peter","age":3},{"index":3,"type":null,"author":"peter","age":4},{"index":4,"type":null,"author":"mary","age":5},{"index":5,"type":"book","author":"mary","age":6}]}
