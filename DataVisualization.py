import pandas as pd
from matplotlib import pyplot

dataset = pd.read_csv('pollution.csv', header = 0, index_col = 0)
values = dataset.values

groups = [0, 1, 2, 3, 4, 5, 6, 7]
i = 1
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups),1,i)
    pyplot.plot(values[:,group])
    pyplot.title(dataset.columns[group], y=0.5, loc = 'right')
    i+=1
pyplot.show()