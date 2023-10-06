from cvxopt.modeling import variable, op
import time

start = time.time()

x = variable(2, 'x')
z = -(2 * x[0] - x[1])  # Функция цели

# Ограничения
mass1 = (x[0] <= 3)  # x1 <= 3
mass2 = (x[0] >= -1)  # x1 >= -1
mass3 = (-2 * x[0] - 3 * x[1] <= 6)  # -2*x1 - 3*x2 <= 6
mass4 = (-x[0] + 2 * x[1] <= 6)  # -x1 + 2*x2 <= 6
x_non_negative = (x >= 0)  # x неотрицательные

problem = op(z, [mass1, mass2, mass3, mass4, x_non_negative])
problem.solve(solver='glpk')

problem.status

print("Максимальная прибыль:")
print(abs(problem.objective.value()[0]))
print("Результат:")
print(x.value)

stop = time.time()
print("Время :")
print(stop - start)

