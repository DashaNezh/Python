# решение ду при помощи метода эйлера(Бояршинов М. Г. "Численные методы")
import numpy as np
import matplotlib.pyplot as plt


# x_0 - принимает начальные условия
# h - шаг
# t_end - время, до которого производится чис. интегрирование

# функция для решения дифференциального уравнения методом Эйлера
def solve_euler_method(f, x_0, h, t_end):
    t_values = np.arange(0, t_end, h)  # массив t
    x_values = np.zeros_like(t_values)  # массив значений х
    x_dot_values = np.zeros_like(t_values)  # массив значений x'

    # устанавливаем начальные условия
    x_values[0] = x_0[0]  # начальное значение х
    x_dot_values[0] = x_0[1]  # начальное значение производной

    for i in range(1, len(t_values)):
        x = x_values[i - 1]
        x_dot = x_dot_values[i - 1]
        x_ddot = f(x, x_dot, t_values[i])

        # вычисляем новые значения x и x'
        x_values[i] = x + h * x_dot
        x_dot_values[i] = x_dot + h * x_ddot

    return t_values, x_values, x_dot_values


# уравнение a: x''(t) + x(t) = 0
def equation_a(x, x_dot, t):
    return -x


# уравнение b: x'' + x = t
def equation_b(x, x_dot, t):
    return t - x


# уравнение c: x'' + x = sin(t)
def equation_c(x, x_dot, t):
    return np.sin(t) - x


# аналитическое решение уравнения a
def analytical_solution_a(t):
    return np.cos(t) + np.sin(t)


# аналитическое решение уравнения b
def analytical_solution_b(t):
    return t - np.sin(t)


# аналитическое решение уравнения c
def analytical_solution_c(t):
    return 1 / 2 * (-t * np.cos(t) + np.sin(t))


# функция для вычисления погрешности
# numerical_solution - численное решение
# analytical_solution - аналитическое решение
def compute_error(numerical_solution, analytical_solution):
    return np.abs(numerical_solution - analytical_solution)


def main():
    # параметры для численного решения
    h = 0.0001  # Шаг интегрирования
    t_end = 10  # Конечное время

    # начальные условия для каждого уравнения
    initial_condition_a = [1, 1]  # x(0) = 1, x'(0) = 1
    initial_condition_b = [0, 0]  # x(0) = 0, x'(0) = 0
    initial_condition_c = [0, 0]  # x'(0) = 0

    # решение уравнения a
    t_values_a, x_values_a, _ = solve_euler_method(equation_a, initial_condition_a, h, t_end)
    error_a = compute_error(x_values_a, analytical_solution_a(t_values_a))

    # решение уравнения b
    t_values_b, x_values_b, _ = solve_euler_method(equation_b, initial_condition_b, h, t_end)
    error_b = compute_error(x_values_b, analytical_solution_b(t_values_b))

    # решение уравнения c
    t_values_c, x_values_c, _ = solve_euler_method(equation_c, initial_condition_c, h, t_end)
    error_c = compute_error(x_values_c, analytical_solution_c(t_values_c))

    # построение графиков

    plt.figure(figsize=(14, 8))

    plt.subplot(3, 2, 1)
    plt.plot(t_values_a, x_values_a, label='Численное решение')
    plt.plot(t_values_a, analytical_solution_a(t_values_a), label='Аналитическое решение')
    plt.xlabel('t')
    plt.ylabel('Значение')
    plt.title('Решение для x\'\'(t) + x(t) = 0')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 2, 2)
    plt.plot(t_values_a, error_a, label='Ошибка')
    plt.xlabel('t')
    plt.ylabel('Значение')
    plt.title('Ошибка для x\'\'(t) + x(t) = 0')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 2, 3)
    plt.plot(t_values_b, x_values_b, label='Численное решение')
    plt.plot(t_values_b, analytical_solution_b(t_values_b), label='Аналитическое решение')
    plt.xlabel('t')
    plt.ylabel('Значение')
    plt.title('Решение для x\'\'(t) + x(t) = t')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 2, 4)
    plt.plot(t_values_b, error_b, label='Ошибка')
    plt.xlabel('t')
    plt.ylabel('Значение')
    plt.title('Ошибка для x\'\'(t) + x(t) = t')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 2, 5)
    plt.plot(t_values_c, x_values_c, label='Численное решение')
    plt.plot(t_values_c, analytical_solution_c(t_values_c), label='Аналитическое решение')
    plt.xlabel('t')
    plt.ylabel('Значение')
    plt.title('Решение для x\'\'(t) + x(t) = sin(t)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 2, 6)
    plt.plot(t_values_c, error_c, label='Ошибка')
    plt.xlabel('t')
    plt.ylabel('Значение')
    plt.title('Ошибка для x\'\'(t) + x(t) = sin(t)')
    plt.grid(True)
    plt.legend()

    plt.subplots_adjust(hspace=0.5, wspace=0.3)
    plt.show()


if __name__ == "__main__":
    main()