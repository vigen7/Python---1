#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Виген Осипов
#
# Created:     23.10.2018
# Copyright:   (c) v.osipov 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a = int(input("Введите число 1:"))
b = int(input("Введите число 2:"))

a,b = b,a
print(a)
print(b)
