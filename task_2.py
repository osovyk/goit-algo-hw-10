import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

def monte_carlo_integration(f, a, b, n):
    max_y = max(f(x))
    count = 0

    for _ in range(n):
        x_rand = random.uniform(a, b)
        y_rand = random.uniform(0, max_y)
        if y_rand <= f(x_rand):
            count += 1

    # Площа прямокутника
    area_rectangle = (b - a) * max_y
    # Оцінка інтеграла
    integral = area_rectangle * count / n

    return integral

# Обчислення інтеграла методом Монте-Карло
n = 1000000
monte_carlo_result = monte_carlo_integration(f, a, b, n)

# Аналітичне значення інтеграла (для квадратичної функції)
analytical_result = (b**3 - a**3) / 3

# Обчислення інтеграла
quad_result, error = spi.quad(f, a, b)

# Виведення результатів
print("Результат за методом Монте-Карло:", monte_carlo_result)
print("Аналітичний результат:", analytical_result)
print("Результат за допомогою quad:", quad_result)

# Порівняння результатів
print("Відносна похибка Монте-Карло:", abs(monte_carlo_result - analytical_result) / analytical_result)