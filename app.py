from Sort import execution_time_gathering


if __name__ == "__main__":
    minimum_size = 100
    maximum_size = 500
    step = 50
    samples_by_size = 10

    table = execution_time_gathering.take_execution_time(
        minimum_size, maximum_size, step, samples_by_size
    )

    print("Size | BubbleSort | InsertionSort | MergeSort | QuickSort | CountingSort")
    for row in table:
        print(row)