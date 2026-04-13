def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
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
    
    for bucket in buckets:
        insertion_sort(bucket)
    
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1