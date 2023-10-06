from scipy.optimize import linprog 
import time 

start = time.time() 

c = [-2, 1]  # Функция цели 
A_ub = [[1, 0], [-1, 0], [-2, -3], [-1, 2]]  
b_ub = [3, 1, -6, 6]  
A_eq = []  
b_eq = []  

result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs')

print(result)

stop = time.time() 
print("Время :") 
print(stop - start)

