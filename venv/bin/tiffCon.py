#converts TIFF images to arrays
import matplotlib.pyplot as plt
import numpy


img_arr = plt.imread("Lepton_Capture_2.tiff")

plt.imshow(img_arr)
plt.show()
img_arr2 = numpy.array(img_arr)
print(img_arr2)
print(img_arr2.shape)
np_im =img_arr2 - 18.
new_im = Image. fromarray(np_im)
new_im. save("numpy_altered_sample2.png")

""""

from PIL import Image
import numpy
import PIL


im = Image.open('Lepton_Capture_2.tiff')
im.show()

imarray = numpy.array(im)

f= open("guru99.txt","w+")
for i in range(0,imarray.shape[0]):

  for j in range(0,imarray.shape[1]):
      f.write(str(imarray[i,j])+" ")
  f.write("\n")

f.close()"""



