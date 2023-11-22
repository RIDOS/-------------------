import matplotlib.pyplot as plt
import os
from math import pi, cos, sin


def plot_parametric_curve():
    # Вычисляем шаг h
    h = (pi * cos(2)) / 100

    # Создаем списки для хранения значений x и y
    x_values = []
    y_values = []

    # Вычисляем значения x и y для каждого шага
    for i in range(1000):
        x = cos(h) + h * sin(h)
        y = sin(h) - h * cos(h)
        x_values.append(x)
        y_values.append(y)
        h += (pi * cos(2)) / 100

    # Строим график
    plt.figure(figsize=(6, 6))
    plt.plot(x_values, y_values, label='График')

    # Перемещаем начало координат в центр графика
    plt.gca().spines['left'].set_position('zero')
    plt.gca().spines['bottom'].set_position('zero')
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')

    # Добавляем подписи к осям
    plt.xlabel('x')
    plt.ylabel('y')

    # Добавляем подписи формул x и y
    plt.text(0.5, -3, r'$x = \cos(h) + h \cdot \sin(h)$', fontsize=12)
    plt.text(0.5, -5, r'$y = \sin(h) - h \cdot \cos(h)$', fontsize=12)

    # Добавляем заголовок
    plt.title('Параметрическая кривая', fontsize=14, loc='center')

    # Добавляем клетки для вспомогательной сетки
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')

    plt.legend()

    # Создаем папку 'img', если её нет
    img_folder = 'img'
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    # Сохраняем график в формате SVG в папке 'img'
    plt.savefig(os.path.join(img_folder, 'parametric_curve.svg'), format='svg')

    plt.show()
