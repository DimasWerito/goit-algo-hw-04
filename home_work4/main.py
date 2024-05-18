"""
Comparing time efficiency of Insertion Sort and Merge Sort algorithms
"""


import random
import timeit

# Функція для генерації випадкових масивів
def generate_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Вимірювання часу сортування
def benchmark_sorting_algorithms():
    sizes = [100, 1000, 10000]
    results = {'Insertion Sort': [], 'Merge Sort': [], 'Timsort': []}
    for size in sizes:
        arr = generate_array(size)
        # Отримуємо час виконання для insertion sort
        insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
        results['Insertion Sort'].append(insertion_sort_time)
        
        # Отримуємо час виконання для merge sort
        merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
        results['Merge Sort'].append(merge_sort_time)
        
        # Отримуємо час виконання для вбудованого sort (Timsort)
        timsort_time = timeit.timeit(lambda: sorted(arr.copy()), number=1)
        results['Timsort'].append(timsort_time)

    return results

# Виведемо результати в консоль
results = benchmark_sorting_algorithms()

# Форматування виводу для кращого читання
print("Час виконання алгоритмів сортування (секунди):")
print("Розміри масивів: [100, 1000, 10000]")
for algorithm, times in results.items():
    print(f"{algorithm}: {times}")