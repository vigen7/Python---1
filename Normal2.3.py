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
import random
n = int(input("Введите количество аргументов"))
a = []
i = 1
while i <= n:
    a.append(random.randint(-100,100))
    i += 1
print(a)


