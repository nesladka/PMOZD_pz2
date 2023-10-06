import pulp
import time

start = time.time()

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += 2 * x1 - x2, "Функция цели"
problem += x1 <= 3, "1"
problem += x1 >= -1, "2"
problem += -2 * x1 - 3 * x2 <= 6, "3"
problem += -x1 + 2 * x2 <= 6, "4"

problem.solve()

print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)

print("Прибыль:")
print(pulp.value(problem.objective))

stop = time.time()
print("Время :")
print(stop - start)
