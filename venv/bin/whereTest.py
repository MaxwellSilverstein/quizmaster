import numpy as np

qq = np.array([3,8,3,5,6,7,4,3,4,6])

find = list(np.where(qq == min(qq))[0])
print(find)
Frames_Temp_max= (find[0])
print(Frames_Temp_max)