# figure & sublplt

from matplotlib import pyplot as plt

"""
1. matplotlib 에서 그래프는 figure객체내에 존재한다.
"""


fig = plt.figure()
splt1 = fig.add_subplot(1, 1, 1)

splt1.plot([2, 4, 5, 6], [81, 93, 91, 97])

plt.show()

