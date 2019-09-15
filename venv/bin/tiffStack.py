from PIL import Image, ImageSequence

#read multi-page TIFF through slicing. you need to know the number of images for this to work. the enumerator you do NOT
im = Image.open("Lepton_Capture_5.tiff")

for i, page in enumerate(ImageSequence.Iterator(im)):
    page.save("page%d.png" % i)
#new
from PIL import Image
import numpy as np

def read_tiff(path, n_images):
    """
    #path - Path to the multipage-tiff file
   # n_images - Number of pages in the tiff file
    """
    img = Image.open("Lepton_Capture_5.tiff")
    images = []
    for i in range(n_images):
        try:
            img.seek(i)
            slice_ = np.zeros((img.height, img.width))
            for j in range(slice_.shape[0]):
                for k in range(slice_.shape[1]):
                    slice_[j,k] = img.getpixel((j, k))

            images.append(slice_)
            print(slice_)
        except EOFError:
            # Not enough frames in img
            break

    return np.array(images)
#new way to read it through itk but as one image
from skimage import io
im = io.imread('Lepton_Capture_5.tiff')
print(im.shape)
image = itk.imread('Lepton_Capture_5.tiff')
im.show(image)