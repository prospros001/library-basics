# scatter() 함수: 산포도 그리기
from matplotlib import pyplot as plt

heights = [100, 120, 130, 140, 150, 160, 170, 180, 190]
footsizes = [200, 205, 210, 220, 230, 250, 270, 280, 285]

fig, sp = plt.subplots()
sp.scatter(heights, footsizes)

plt.xlabel('Hegiht(Cm)')
plt.ylabel('Foot Size(Cm)')
plt.show()
