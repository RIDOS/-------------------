from src.parametric_curve import plot_parametric_curve
from src.polar_curve import plot_polar_curve


def main():
    """
    Разработал: Имаев Азат
    Группа: ПИ-41

    Построение графиков и сохранения их в формате SVG.
    """

    # Параметрическая кривая.
    plot_parametric_curve()

    # Полярная кривая.
    plot_polar_curve()


if __name__ == '__main__':
    main()
