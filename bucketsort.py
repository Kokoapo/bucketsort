def insertion_sort(arr):
    size = len(arr)
    key = arr[size-1]
    j = size - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

def bucket_sort(arr, n_buckets):
    n = len(arr)
    buckets = [[] for _ in range(n_buckets)]

    for num in arr:
        bi = int((num/n) * n_buckets)
        buckets[bi].append(num)
        insertion_sort(buckets[bi])
    
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1