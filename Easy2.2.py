#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      v.osipov
#
# Created:     25.10.2018
# Copyright:   (c) v.osipov 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a = [1, 2, 3, 5, 6]
b = [3, 4, 6, 9, 10]

for c in b:
    if c in a:
        a.remove(c)
print(a)
