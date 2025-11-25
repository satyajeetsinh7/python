# Write a Python program to display details of an image (dimension of an image, shape of an image, min pixel value at channel B).

from PIL import Image
import numpy as np

img = Image.open(r"D:\Colleg\Python\EX\Image.jpg")
img_array = np.array(img)

print("Image Size (width x height):", img.size)
print("Image Shape (H x W x C):", img_array.shape)
print("Minimum Pixel Value at Channel B:", img_array[:, :, 2].min())

# Write a Python program to padding black spaces 
from PIL import Image, ImageOps

img = Image.open(r"D:\Colleg\Python\EX\Image.jpg")
padded_img = ImageOps.expand(img, border=50, fill="black")
padded_img.show()

# Write a Python program to visualize RGB channels 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"D:\Colleg\Python\EX\Image.jpg")
img_array = np.array(img)

R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(R, cmap="Reds")
plt.title("Red Channel")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(G, cmap="Greens")
plt.title("Green Channel")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(B, cmap="Blues")
plt.title("Blue Channel")
plt.axis("off")

plt.show()