#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      v.osipov
#
# Created:     24.10.2018
# Copyright:   (c) v.osipov 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
Fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 0

for el in Fruits:
    print('{}.{:>8}'.format(i,el))
    i += 1