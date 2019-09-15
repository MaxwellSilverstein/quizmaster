import tiffcapture as tc
import cv2
import numpy as np
from PIL import Image, ImageSequence
from datetime import datetime
import struct
import sys
def main():
    print(sys.argv[1])
    tiff = tc.opentiff(sys.argv[1])
    print(sys.getsizeof(open(sys.argv[1])))
    i = 0
    for img in tiff:
        if i ==30:
            print(sys.getsizeof(img))
            img_arr = np.array(img, dtype='int64')

            print(img_arr[103,110])
            img_arr = img_arr - 27315
            print(img_arr[103, 110])


            dt = np.dtype('int16')
            img_arr = np.array(img, dtype=dt)
            print(img_arr[103, 110])
            img_arr= img_arr - 27315
            print(img_arr[103, 110])


        i += 1


if __name__ == "__main__":
    main()
