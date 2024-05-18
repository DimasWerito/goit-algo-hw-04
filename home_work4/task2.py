"""
Дано k відсортованих списків цілих чисел. Ваше завдання — 
об'єднати їх у один відсортований список. 
При виконанні завдання можете опиратися на алгоритм сортування злиттям з конспекту. 
Реалізуйте функцію merge_k_lists , яка приймає на вхід список відсортованих списків та повертає відсортований список.
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
Виведення:
Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
"""


import heapq

def merge_k_lists(lists):
    # Ініціалізуємо пріоритетну чергу
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            # Додаємо перший елемент з кожного списку разом з індексом списку та індексом елемента у списку
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged_list = []
    # Доки в черзі є елементи
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        
        # Якщо в списку є ще елементи, додаємо наступний у чергу
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list

# Тестування функції
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
