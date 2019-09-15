#first TIFF to HT Script
import tiffcapture as tc
import cv2
import numpy as np
from PIL import Image, ImageSequence
from datetime import datetime
import struct



def filePacker(filePath,versionId, patientId, testId, frameWidth, frameHeight, frameNumber, decayPoint, heatingPoint,outFile):
            dateTimeObj = datetime.now()
            now = dateTimeObj.strftime("%d%m%Y%H%M%S")#ddMMyyyyHHmmss
            dateX = now.encode(encoding = 'ascii',errors='strict')
            tiff = tc.opentiff(filePath) #open img
            outputFile = open(outFile,"wb")
            outputFile.write(struct.pack('B',versionId))
            outputFile.write(struct.pack('i',patientId))
            outputFile.write(struct.pack('i',testId))
            outputFile.write(struct.pack('14B',*dateX))
            outputFile.write(struct.pack('i',frameWidth))
            outputFile.write(struct.pack('i',frameHeight))
            outputFile.write(struct.pack('i',frameNumber))
            outputFile.write(struct.pack('i',decayPoint))
            outputFile.write(struct.pack('i',heatingPoint))
            frameLooper(tiff,outputFile,frameWidth,frameHeight)
            outputFile.close()

def frameLooper(tiffX,fileOut,frameWidth,frameHeight):
     frameNumber =0
     for img in tiffX:
                 #loop through frames
                 dt = np.dtype('int16')
                 img_arr = np.array(img,dtype = dt)#read into nparray
                 img_arr = (img_arr)-27330 #convert to HT Bio style temps
                 #  np.savetxt("Capture%d.csv" %i,img_arr,delimiter = ",",fmt=('%f'))
                 #here we could append the files together
                 flatImg = img_arr.flatten()
                 fileOut.write(struct.pack('i',frameNumber))
                 fileOut.write(struct.pack("%dh"%(frameWidth*frameHeight),*flatImg))
                 frameNumber+=1

def main():
    #_, first_img = tiff.retrieve()
    file = "Lepton_Capture_5.tiff"
    #frameNumber = 0 #frame Number
    version = 2
    patient = 4
    test = 1
    width = 160
    height = 120
    frame = 170
    decay = 170
    heat = 27
    out = "bwFile.HTBio"
    filePacker(file,version,patient,test,width,height,frame,decay,heat,out)

if __name__ == "__main__":
    main()


#from PIL import Image
#import numpy
#im = Image.open("Lepton_Capture_5.tiff")
#np_im = numpy.array(im)
#print(np_im[0,0])