import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

### loading meta.csv table

table = pd.read_csv("../MiceNasa/train/meta.csv")

##ratio based on radiation type
type1 = table[table['particle_type']=="X-ray"]
type2 = table[table['particle_type']=="Fe"]
count = [type1.size,type2.size]
mylabels = ["X-ray", "Fe"]
plt.pie(count,labels=mylabels)
plt.show()
ratio = count/np.sum(count)
print(ratio)



#### distribution considering dose_Gy
table.groupby('particle_type')['dose_Gy'].plot(kind='kde')
plt.xlabel('dose_Gy')
plt.legend(['Fe','X-ray'])
plt.show()


###distribution considering  hr_post_exposure

table.groupby('particle_type')['hr_post_exposure'].plot(kind='hist')
plt.xlabel('Hr Post Exposure')
plt.legend(['Fe','X-ray'])
plt.show()




table['hr_post_exposure'].plot(kind='hist')
plt.xlabel('Hr Post Exposure')
#plt.legend(['Fe','X-ray'])
plt.show()






