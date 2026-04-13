def bucket_sort(arr, n_buckets):
    n = len(arr)
    buckets = [[] for _ in range(n_buckets)]

    for num in arr:
        bi = int((num/n) * n_buckets)
        print(bi)
        buckets[bi].append(num)
    
    for bucket in buckets:
        print(bucket)