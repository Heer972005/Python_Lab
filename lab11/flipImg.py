import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r'G:\sem-3\python_lab\lab11\Screenshot 2025-08-31 163932.png')
img_array = np.array(img)
flipped_img = np.fliplr(img_array)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(flipped_img )
plt.title('Flipped Image')
plt.axis('off')
plt.tight_layout()
plt.show()