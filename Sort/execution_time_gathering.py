import time


from Sort import algorithms
from Sort import constants
from Sort import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return five values, one per algorithm: The execution time
"""


def take_times(size, samples_by_size):
    samples = [
        data_generator.get_random_list(size) for _ in range(samples_by_size)
    ]

    return [
        take_time_for_algorithm(samples, algorithms.bubble_sort),
        take_time_for_algorithm(samples, algorithms.insertion_sort),
        take_time_for_algorithm(samples, algorithms.merge_sort),
        take_time_for_algorithm(samples, algorithms.quick_sort),
        take_time_for_algorithm(samples, algorithms.counting_sort),
    ]


"""
    Returns the median of the execution time
"""


def take_time_for_algorithm(samples, algorithm):
    times = []

    for sample in samples:
        start = time.time()
        algorithm(sample.copy())
        end = time.time()
        times.append(constants.TIME_MULTIPLIER * (end - start))

    times.sort()
    return times[len(times) // 2]
