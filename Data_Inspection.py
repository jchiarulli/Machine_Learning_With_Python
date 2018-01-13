import numpy as np
import matplotlib.pyplot as plt
from Load_Data import images, labels

images = np.array(images)
labels = np.array(labels)

# Print the 'images' dimensions
print(images.ndim)

# Print the number of 'images' elements
print(images.size)

# Print the first instance of 'images'
print(images[0])

# Print the 'labels' dimensions
print(labels.ndim)

# Print the number of 'labels' elements
print(labels.size)

# Count the number of labels
print(len(set(labels)))

# Make a histogram with 62 bins of the 'labels' data
plt.hist(labels, 62)

# Show the plot
plt.show()

print("Flags \n{} \n Item Size : {} \n Nbytes : {}".format(images.flags, images.itemsize,
      images.nbytes))
