# 색상, 마커, 선 스타일

'''
 plot 메서드는 그래프이 색상과 스타일 마커등을 문자열로 표현하여 인자로 넘겨줄 수 있다.

 color
 복합 문자열 전달 : k, r, b, g, y, ..
 명시적 표현 전달 : balck, red, blue, gree, yellow
 cf) #rrggbb도 가능 #00000
 linestyle :  - (solid), - - (dashed), -.(dashdot), ''(None)
 marker : .(dot) v(화살표, o(big dot)


'''


from matplotlib import pyplot as plt

fig, sp = plt.subplots(1, 1)
sp.plot([1,2,3,4], [10, 20, 30, 40], color='#000', linestyle='None', marker='.')
plt.show()