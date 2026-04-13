from bucketsort import bucket_sort
import sys
import random

def start_array(size):
    arr = []
    for _ in range(size):
        arr.append(random.randint(0, size-1))
    return arr

def print_erro():
    print('Parâmetros Inválidos!')
    print('python main.py <tamanho do vetor> <número de baldes>')
    print('1 <= tamanho do vetor <= 1000000')
    print('1 <= número de baldes <= tamanho do vetor')

    exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_erro()
    try:
        size = int(sys.argv[1])
        buckets = int(sys.argv[2])
    except:
        print_erro()
    if size < 1 or size > 1000000 or buckets < 1 or buckets > size:
        print_erro()
    
    arr = start_array(size)
    bucket_sort(arr, buckets)