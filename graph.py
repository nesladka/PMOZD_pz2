import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-8, 4, 100)
x2 = np.linspace(-8, 4, 100)

X1, X2 = np.meshgrid(x1, x2)

plt.figure(figsize=(8, 6))
plt.xlabel('x1')
plt.ylabel('x2')


plt.plot(x1, 3 * np.ones_like(x1), label='x1 <= 3', color='blue', linestyle='dotted')
plt.plot(x1, -1 * np.ones_like(x1), label='x1 >= -1', color='purple', linestyle='dotted')
plt.plot(x1, (6 + 2 * x1) / -3, label='-2*X1 - 3*X2 <= 6', color='orange', linestyle='dotted')
plt.plot(x1, (6 + x1) / 2, label='-X1 + 2*X2 <= 6', color='green', linestyle='dotted')

plt.arrow(0, 0, -2, 1, head_width=0.3, head_length=0.5, fc='red', ec='red', label='вектор z')

perpendicular_x = np.array([-1, 1])
perpendicular_y = np.array([-2, 2])

plt.plot(perpendicular_x, perpendicular_y, linestyle='-.', color='cyan', label='перпендикуляр')

plt.title('Линейная функция')

plt.text(2, 3.1, 'x1 <= 3', fontsize=10, color='blue', rotation=0)
plt.text(2, -0.9, 'x1 >= -1', fontsize=10, color='purple', rotation=0)
plt.text(-3, -1, '-2*X1 - 3*X2 <= 6', fontsize=10, color='orange', rotation=-30)
plt.text(0, 3.3, '-X1 + 2*X2 <= 6', fontsize=10, color='green', rotation=25)

plt.fill_between([-8 , -1.5,-4.286, -8], [-1 , -1,0.855,-1], color='lavender')

plt.grid(True)
plt.legend()
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show() 

