# scatter() 함수 : 산포도 그리기


from matplotlib import pyplot as plt

height = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200]
footsizes = [200, 205, 210, 220, 230, 240, 250, 270, 280, 285]

fig, sp = plt.subplots()
sp.scatter(height, footsizes)

plt.xlabel('Heith(cm)')
plt.ylabel('Foot size(cm)')


plt.show()