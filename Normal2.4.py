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

a = [1, 5, 4, 9, 4]
b = []
for c in a:
    if c not in b:
        b.append(c)
print(b)

a = [1, 5, 4, 9, 4]
b = []
for c in a:
    if a.count(c) == 1:
        b.append(c)
print(b)