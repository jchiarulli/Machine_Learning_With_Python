from skimage import transform
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from Load_Data import images, labels

# Rescale the images in the 'images' array
images28 = [transform.resize(image, (28, 28)) for image in images]
# print(np.array(images28).shape)

# Determine the (random) indexes of the images that you want to see
traffic_signs = [300, 2250, 3650, 4000]

# Fill out the subplots with the random images that you defined
'''for i in range(len(traffic_signs)):
    plt.subplot(1, 4, i+1)
    plt.axis('off')
    plt.imshow(images28[traffic_signs[i]])
    plt.subplots_adjust(wspace=0.5)
    plt.show()
    print("shape: {0}, min: {1}, max: {2}".format(images28[traffic_signs[i]].shape,
          images28[traffic_signs[i]].min(), images28[traffic_signs[i]].max()))'''

# Convert 'images28' to an array
images28 = np.array(images28)

# Convert 'images28' to grayscale
images28 = rgb2gray(images28)

for i in range(len(traffic_signs)):
    plt.subplot(1, 4, i+1)
    plt.axis('off')
    plt.imshow(images28[traffic_signs[i]], cmap="gray")
    plt.subplots_adjust(wspace=0.5)
    
plt.show()
