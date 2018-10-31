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
a = [1, 2, 3, 4, 5, 6, 7]
b = []
for c in a:
    if c % 2 == 0:
        b.append(c/4)
    else:
        b.append(c*2)
print(b)