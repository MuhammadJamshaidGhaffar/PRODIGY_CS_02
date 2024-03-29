import sys
from PIL import Image
import numpy as np
import os

if(len(sys.argv) < (1+2)):
    print(f"Usage : {sys.argv[0]} <image_path> <key>")
    exit(1)

image_path = sys.argv[1]
key = int(sys.argv[2])

image = Image.open(image_path)
image_array = np.array(image)
image_array = image_array ^ key
new_image = Image.fromarray(image_array.astype('uint8'))

# save the new image
directory, filename = os.path.split(image_path)
name , extension = os.path.splitext(filename)
new_image_name = f"manipulated_{name}{extension}"
new_image_path = os.path.join(directory, new_image_name)
new_image.save(new_image_path)
new_image.show()



