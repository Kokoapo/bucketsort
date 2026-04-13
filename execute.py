from bucketsort import bucket_sort
import random, time

def start_array(size):
    arr = []
    for _ in range(size):
        arr.append(random.randint(0, size-1))
    return arr

def execute(size, buckets):
    arr = start_array(size)

    start_time = time.time()
    bucket_sort(arr, buckets)
    end_time = time.time()

    return end_time-start_time