import sys

def start_array(size):
    arr = []
    for i in range(size):
        arr.append(i)
    return arr

def shuffle_array():
    pass

def print_erro():
    print('Parâmetros Inválidos!')
    print('python main.py <tamanho do vetor> <número de baldes>')
    print('1 <= tamanho do vetor <= 1000000')
    print('1 <= número de baldes <= 100')

    exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_erro()
    try:
        size = int(sys.argv[1])
        buckets = int(sys.argv[2])
    except:
        print_erro()
    if size < 1 or size > 1000000 or buckets < 1 or buckets > 100:
        print_erro()
    
    arr = start_array(size)
    