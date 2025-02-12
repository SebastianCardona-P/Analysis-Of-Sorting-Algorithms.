# Big O complexity analysis


# n is the size of arr
def bubble_sort(arr):
    n = len(arr)  # O(1)
    for i in range(n):  # O(n)
        for j in range(n - i - 1):  # O(n)
            if arr[j] > arr[j + 1]:  # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1)
    return arr  # O(1)


# O(bubble_sort) = O(1 + n * n + 1 + 1)
# = O(n^2 + 3) = O(n^2)


# n is the size of arr
def merge_sort(arr):
    if len(arr) > 1:  # O(1)
        mid = len(arr) // 2  # O(1)
        left = arr[:mid]  # O(n)
        right = arr[mid:]  # O(n)

        merge_sort(left)  # O(T(n/2))
        merge_sort(right)  # O(T(n/2))

        i = j = k = 0  # O(1)
        # merge arrays
        while i < len(left) and j < len(right):  # O(n)
            if left[i] < right[j]:  # O(1)
                arr[k] = left[i]  # O(1)
                i += 1  # O(1)
            else:
                arr[k] = right[j]  # O(1)
                j += 1  # O(1)
            k += 1  # O(1)

        # Put the remainder of the left array
        while i < len(left):  # O(n)
            arr[k] = left[i]  # O(1)
            i += 1  # O(1)
            k += 1  # O(1)

        # Put the remainder of the right array
        while j < len(right):  # O(n)
            arr[k] = right[j]  # O(1)
            j += 1  # O(1)
            k += 1  # O(1)

    return arr  # O(1)


# O(merge_sort) = Master theorem
# T(n) = 2 * T(n/2) + O(n)
# A = 2, B = 2, C = 1
# log_B(A) = log_2(2) = 1
# O(merge_sort) = O(n * log(n))


# n is the size of arr
def insertion_sort(arr):
    for i in range(1, len(arr)):  # O(n)
        key = arr[i]  # O(1
        j = i - 1  # O(1)

        while j >= 0 and key < arr[j]:  # O(n)
            arr[j + 1] = arr[j]  # O(1)
            j -= 1  # O(1)

        arr[j + 1] = key  # O(1)

    return arr  # O(1)


# O(insertion_sort) =
# O(n * n) = O(n^2)


# n is the size of arr
def quick_sort(arr):
    if len(arr) <= 1:  # O(1)
        return arr  # O(1)

    pivot = arr[len(arr) // 2]  # O(1)
    left = [x for x in arr if x < pivot]  # O(n)
    middle = [x for x in arr if x == pivot]  # O(n)
    right = [x for x in arr if x > pivot]  # O(n)
    return quick_sort(left) + middle + quick_sort(right)  # O(T(n/2))


# O(quick_sort) = Master theorem
# T(n) = 2 * T(n/2) + O(n)
# A = 2, B = 2, C = 1
# log_B(A) = log_2(2) = 1
# O(quick_sort) = O(n * log(n))


# n is the size of arr
def counting_sort(arr):

    if len(arr) == 0:
        return arr  # O(1)

    # Extract the maximum value from the list
    max_value = max(arr)  # O(n)

    # Create a list to store the count of each element
    count = [0] * (max_value + 1)  # O(k)

    # Count the number of times each element appears
    for number in arr:  # O(n)
        count[number] += 1  # O(1)

    # Build the sorted list
    new_arr = []  # O(1)

    for i in range(max_value + 1):  # O(k)
        new_arr.extend([i] * count[i])  # O(1)

    return new_arr  # O(1)


# O(counting_sort) =
# O(n + k + n + k + 1) = O(2n + 2k + 1) = O(n + k)
