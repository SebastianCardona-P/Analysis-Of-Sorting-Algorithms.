from Sort import execution_time_gathering


if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 10100
    step = 1000
    samples_by_size = 10

    table = execution_time_gathering.take_execution_time(
        minimum_size, maximum_size, step, samples_by_size
    )

    print("Size | BubbleSort | InsertionSort | MergeSort | QuickSort | CountingSort")
    for row in table:
        print(row)