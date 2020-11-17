# 색상, 마커, 선스타일
"""
    plot 메서드에 문자열 인자 전달은 의미전달과 복잡해 보이기 때문에 잘 사용하지 않고 다음과 같이 명시적 방법을 선호한다.
    color
    복합 문자열 전달:     k, r,    b,    g,   y,      ....
    명시적 표현 전달: balck, red, blue, gree, yellow, ....
    cf) #rrggbb도 가능  #000000 #ff0000, #0000ff, #00ff00, #00ffff
    linestyle : - (solid), --(dashed), -.(dashdot), dotted, ‘ ‘(None)
    marker : .(dot) v(화살표), o(big dot)
"""
from matplotlib import pyplot as plt

fig, sp = plt.subplots(1, 1)
sp.plot([1, 2, 3, 4], [10, 20, 30, 40], color='#000', lineStyle=' ', marker='.')

plt.show()