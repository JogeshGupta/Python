import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0,256,size = (256,256))
print(x)

plt.subplot(1,2,1)
plt.imshow(x,cmap = 'gray')
plt.title('Original Image')
plt.axis('off')
plt.show()