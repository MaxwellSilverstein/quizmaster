#Modified TIFF To HT Script

import cv2
import numpy as np
from PIL import Image, ImageSequence
from datetime import datetime
import struct
import sys
from pathlib import Path
#filePacker opens outFile
# and packs all of the parameters into the header except filePath and itself
#filePath gets opened and read in frameLooper
def filePacker(filePath,versionId, patientId, testId, frameWidth, frameHeight, decayPoint, heatingPoint,outFile):

            #this section creates the date object
            dateTimeObj = datetime.now()
            now = dateTimeObj.strftime("%d%m%Y%H%M%S")#ddMMyyyyHHmmss
            dateX = now.encode(encoding = 'ascii',errors='strict')

            # this section counts the number of frames in the file

            #open tiff file as im
            im = Image.open(filePath)
            print(im.n_frames)
            outputFile = open(outFile,"wb")
            outputFile.write(struct.pack('B',versionId))
            outputFile.write(struct.pack('i',patientId))
            outputFile.write(struct.pack('i',testId))
            outputFile.write(struct.pack('14B',*dateX))
            outputFile.write(struct.pack('i',frameWidth))
            outputFile.write(struct.pack('i',frameHeight))
            outputFile.write(struct.pack('i',(im.n_frames)))#frameNumber-1
            outputFile.write(struct.pack('i',decayPoint))
            outputFile.write(struct.pack('i',heatingPoint))


            #pack into outputfile
            frameLooper(im,outputFile,frameWidth,frameHeight)
            outputFile.close()

#frameLooper goes frame by frame through tiffX and packs the temperature data into fileOut
def frameLooper(tiffX,fileOut,frameWidth,frameHeight):

     for frameNumber, img in enumerate(ImageSequence.Iterator(tiffX)): #loop through frames. note: this loop will not parse a single image
                 #assume TLinear is enabled
                 tLin = True
                 #read into nparray and convert to HT Bio temps
                 dt = np.dtype('int16')
                 img_arr = np.array(img,dtype = dt)


                 #if TLinear is enabled, then we have to convert from degrees K*100 to degrees C*100:
                 if tLin:
                    img_arr = (img_arr)-27315


                 #flatten by rows, add number to the front, and pack the entire array in
                 flatImg = img_arr.flatten()
                 print(frameNumber)
                 print(flatImg[80])
                 fileOut.write(struct.pack('i',frameNumber))
                 fileOut.write(struct.pack("%dh"%(frameWidth*frameHeight),*flatImg))

#main runs file packer taking two file arguments from the command line
#parameters get input here in main
def main():
    # deprecated   _, first_img = tiff.retrieve()
    path =Path("/Users/neilsilverstein/Downloads/BlackBody_Test.tiff")

    file = path  # sys.argv[1]
    version = 2
    patient = 4
    test = 1
    width = 160
    height = 120
    decay = 158
    heat = 38
    out = "BlackBody_Test.HTBio"   # sys.argv[2]
    filePacker(file, version, patient, test, width, height, decay, heat, out)


#./TIFFToHT.py .tiff .HTBio
if __name__ == "__main__":
    main()
