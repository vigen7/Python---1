#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      v.osipov
#
# Created:     27.10.2018
# Copyright:   (c) v.osipov 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
a = [1, 2, 3, 4, 9, 16, 27]
b = []

for c in a:
    if c >= 0:
        if math.sqrt(c).is_integer() == True:
            b.append(int(math.sqrt(c)))
print(b)