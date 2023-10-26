# Бинарный поиск, список считается отсортированным

# Используем структурную и процедурную парадигмы, 
# так как вычисляем искомое пошагово, используя основные конструкции программирования,  
# а также создаём вспомогательную процедуру binary_search.

# Входные данные: список и элемент, который нужно найти
# Выходные данные: индекс искомого элемента

def binary_search(list1, n): 
    left = 0
    right = len(list1)
    while right > left:
        mid = (left + right) // 2
        if list1[mid] == n:
            return mid
        elif list1[mid] < n:
            left = mid+1
        else:
            right = mid
    return -1
 
 
# Проверка 
list1 = [7, 6, 3, 8, 1, 92, 5] 
list1 = sorted(list1)
print(list1)
n = 9 
 
print(binary_search(list1, n))