import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

data = {'type': ['book', 'magazine', None, None, 'book', 'book', 'magazine'],
        'author': ['peter', 'peter', 'peter', 'mary', 'mary', 'mary', 'mary'],
        'age': [1, 2, 3, 5, 6, 7, 8]}
data_frame = pd.DataFrame(data)
groupby = data_frame.groupby('author').size()
print(groupby)

# simple plot
groupby.plot()
plt.show()

# more control on the plot
rcParams.update({'figure.autolayout': True, 'axes.titlepad': 20})
# figure is the container of the subplots
fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)
subplot.set_xlabel("Name")
subplot.set_ylabel("count")
groupby.plot(ax=subplot)
plt.show()

# save figure
fig.savefig('result.png')
