import matplotlib.pyplot as plt
import os
from math import pi, sin


def plot_polar_curve():
    # Создаем списки для хранения значений p и fi
    p_values = []
    fi_values = []

    # Вычисляем значения p и fi для каждого шага
    h = pi / 16
    fi = 0.0
    while fi <= pi / 2:
        p = 2 * sin(2 * fi)
        p_values.append(p)
        fi_values.append(fi)
        fi += h

    plt.figure(figsize=(6, 6))
    plt.polar(fi_values, p_values, label='График')

    # Добавляем заголовок
    plt.title('График в полярных координатах', fontsize=14, loc='center')
    plt.text(-0.9, 0.2, r'$p = 2 \cdot \sin(2 \cdot \phi)$', fontsize=12)
    plt.legend()

    img_folder = 'img'
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    plt.savefig(os.path.join(img_folder, 'polar_curve.svg'), format='svg')
    plt.show()
