import pandas as pd

from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt


### load the metadata

table = pd.read_csv("../MiceNasa/train/meta.csv")

### load image

index = 200
filepath = "../MiceNasa/train"
fname = table.iloc[index].filename
im = imread(filepath+"/"+fname)

plt.imshow(im)
plt.show()




###create intensity histogram
minP = np.min(im)
maxP = np.max(im)
histogram, bin_edges = np.histogram(im, bins=256, range=(minP, maxP))

### plot the histogram

plt.figure()
plt.title("Intensity Histogram")
plt.xlabel("pixel value")
plt.ylabel("pixel count")
plt.xlim([minP, maxP])
plt.plot(bin_edges[0:-1], histogram)
plt.show()











