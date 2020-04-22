import pandas as pd

data1 = pd.read_excel('input1.xlsx')
print(data1)
# output
#  Name  Mark
# 0    Peter    90
# 1     Mary    80
# 2  Vincent    45
# 3      Ivy    78

data2 = pd.read_excel('input2.xlsx')
print(data1)
# output
#      Name  Mark
# 0    Peter    90
# 1     Mary    80
# 2  Vincent    45
# 3      Ivy    78

merged = data1.merge(data2, on='Name')
print(merged)
# output
#       Name  Mark Gender
# 0    Peter    90      M
# 1     Mary    80      F
# 2  Vincent    45      M
# 3      Ivy    78      F

merged.to_excel('merged.xlsx', index=False)

pivot_table = merged.pivot_table(index='Gender', aggfunc='mean')
print(pivot_table)
# output
#         Mark
# Gender
# F       79.0
# M       67.5

pivot_table = merged.pivot_table(index='Gender', aggfunc='max')
print(pivot_table)
# output
#         Mark     Name
# Gender
# F         80     Mary
# M         90  Vincent

pivot_table = merged[['Gender', 'Mark']].pivot_table(index='Gender', aggfunc='max')
print(pivot_table)
# output
#         Mark
# Gender
# F         80
# M         90
