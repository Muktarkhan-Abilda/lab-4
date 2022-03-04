
from math import tan,pi
sides = int(input())
lenghth = int(input())
area = sides*(lenghth ** 2) / (4 * tan(pi/sides))

print(area)