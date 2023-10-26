# Используем функциональную парадигму, так как необходимо вычислить несколько функций.

# 1. Самый простой вариант с использованием встроенной функции 
# библиотеки Numpy

import numpy as np

list1 = [1, 2, 3, 4, 6]
list2 = [2, 4, 6, 8, 10]
 
list3 = np.corrcoef(list1, list2)
#print('Корреляция Пирсона равна: ', list3)

# 2. Вариант с вычислениями 

mean_list1 = sum(list1)/len(list1)
mean_list2 = sum(list2)/len(list2)
def for_difference(x, mean):
    return x - mean
r_1 = map(for_difference(mean_list1), )
print(r_1)