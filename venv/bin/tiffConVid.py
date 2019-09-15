#writes a TIFF video into a text file in row order. this works
import tiffcapture as tc
import cv2
from PIL import Image
import numpy
import PIL
import matplotlib.pyplot as plt

tiff = tc.opentiff("Lepton_Capture_2.tiff") #open img
_, first_img = tiff.retrieve()
cv2.namedWindow('video')
imarray = numpy.array(0)
inc =0
for img in tiff:
    #tempimg = cv2.absdiff(first_img, img) # bkgnd sub
    plt.imshow(img)
    plt.show()
    tempimg = img
    imarray = numpy.array(tempimg)
    np_im = imarray
    new_im = Image.fromarray(np_im)

    new_im.save("numpy_altered_sample_"+str(inc)+".png")
    f = open("guru99.txt", "w+")
    for i in range(0, imarray.shape[0]):

        for j in range(0, imarray.shape[1]):
            f.write(str(imarray[i, j]) + " ")
        f.write("\n")

    f.close()

    cv2.imshow('video', tempimg)
    cv2.waitKey(80)
    inc+=1
cv2.destroyWindow('video')
print(imarray.size)
print(imarray.min())

#np_im = imarray - 18
#new_im = Image.fromarray(np_im)
#new_im.save("numpy_altered_sample2.png")