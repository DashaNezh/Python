import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаем массив значений x, y и z
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X * Y)

# Создаем 3D-график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Построение поверхности
ax.plot_surface(X, Y, Z, alpha=0.5)

# Построение линий ограничений
ax.plot(x, x, zs=0, color='r', linestyle='--')  # y=x
ax.plot([1, 1], [0, 1], [0, 0], color='r', linestyle='--')  # x=1

# Установка ограничений на оси
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Настройка осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графика
plt.show()