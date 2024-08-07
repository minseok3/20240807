import  random
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10,10)

plt.clf()
heatmap = plt.imshow(data, cmap="YlGnBu", aspect='auto')
plt.colorbar(heatmap)
plt.title('Heatmap Example')

plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.savefig("./boxplot.png")
plt.show()
