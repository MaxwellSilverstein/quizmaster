import struct
import numpy as np
import sys
import time
import subprocess
import re
import matplotlib.pyplot as plt
bwx = open("test3.HTBio","rb")
print(struct.unpack("B", bwx.read(1))[0])
print(struct.unpack("i", bwx.read(4))[0])
print(struct.unpack("i", bwx.read(4))[0])
print(struct.unpack("14B", bwx.read(14)))
print(struct.unpack("i", bwx.read(4))[0])
print(struct.unpack("i", bwx.read(4))[0])
print(struct.unpack("i", bwx.read(4))[0])
print(struct.unpack("i", bwx.read(4))[0])
print(struct.unpack("i", bwx.read(4))[0])
print(struct.unpack("i",bwx.read(4))[0])
print(struct.unpack("h",bwx.read(2))[0])
bwx.close()

