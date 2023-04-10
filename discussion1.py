import matplotlib.pyplot as plt
from matplotlib.image import imread

###part1 - showing a color image with matplotlib
im = imread("robin.jpeg")
plt.imshow(im)
plt.title("My Little Bird")
plt.show()
print(im.shape)
print(im)



### part2 - sperating the channels and showing them in subplots
im = imread("robin.jpeg")
fig, axes = plt.subplots(1,3)
Rchannel = im[:,:,0]
Gchannel = im[:,:,1]
Bchannel = im[:,:,2]
axes[0].imshow(Rchannel,cmap='gray')
axes[0].set_title('Red Channel')
axes[1].imshow(Gchannel,cmap='gray')
axes[1].set_title('Green Channel')
axes[2].imshow(Bchannel,cmap='gray')
axes[2].set_title('Blue Channel')
plt.show()

