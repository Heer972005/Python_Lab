import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open(r'G:\sem-3\python_lab\lab11\Screenshot 2025-08-31 163932.png')
img_array=np.array(img)
print(img_array)
y1,x1=100,100
y2,x2=250,200
cropped_img=img_array[y1:y2,x1:x2]
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cropped_img)
plt.title('Cropped Image')
plt.axis('off')
plt.tight_layout()
plt.show()