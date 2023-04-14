import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.image import imread

### loading meta.csv table

table = pd.read_csv("../MiceNasa/train/meta.csv")

# print(table.head())

#### accessing different colomns in pandas
i = 50
print(table.iloc[i].filename)
print(table.iloc[i].dose_Gy)
print(table.iloc[i].particle_type)
print(table.iloc[i].hr_post_exposure)


### showing sample images with matplotlib and cmaps
filepath = "../MiceNasa/train"
fname = table.iloc[i].filename


im = imread(filepath+"/"+fname)
plt.imshow(im,cmap='hot')
plt.show()
print(im.shape)

gy = table[table['dose_Gy']>0.5]
print(gy)


ex = table[table['hr_post_exposure']>=24]
print(ex)

particle = table[table['particle_type']=="X-ray"]
print(particle)






