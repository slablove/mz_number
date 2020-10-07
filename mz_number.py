from numpy.random import *

mzawa_numbers = []
x = int(input("番号を何個生成しますか "))

for k in range(x):
  y = randint(0,9999)
  mzawa_numbers.append(y)

print("前澤ナンバーズ 当選予想番号")
print(mzawa_numbers)