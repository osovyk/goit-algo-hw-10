from pulp import *

# Створення моделі
model = LpProblem("Максимізація виробництва", LpMaximize)

# Змінні
lemonade_quantity = LpVariable("Кількість лимонаду", lowBound=0, cat='Integer')
fruit_juice_quantity = LpVariable("Кількість фруктового соку", lowBound=0, cat='Integer')

# Функція цільова
model += lemonade_quantity + fruit_juice_quantity, "Загальна кількість виробництва"

# Обмеження
model += 2*lemonade_quantity + fruit_juice_quantity <= 100, "Обмеження на воду"
model += lemonade_quantity <= 50, "Обмеження на цукор"
model += lemonade_quantity <= 30, "Обмеження на лимонний сік"
model += 2*fruit_juice_quantity <= 40, "Обмеження на фруктове пюре"

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Статус:", LpStatus[model.status])

for v in model.variables():
    print(v.name, "=", v.varValue)