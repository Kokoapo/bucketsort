import matplotlib.pyplot as plt
from execute import execute

sizes = [100000, 500000, 1000000]
buckets = [1, 10, 100, 1000, 10000, 100000, 1000000]

for size in sizes:
    times = []
    for bucket in buckets:
        final_time = execute(size, bucket)
        times.append(final_time)
        print(f'Tamanho {size} Baldes {bucket} Tempo {final_time}')
    plt.plot(times, buckets)

    plt.yscale('log')

    plt.xlabel('Tempo (Segundos)')
    plt.ylabel('Número de Baldes')
    plt.title(f'Execução para {size} Elementos')

    plt.show()
    plt.savefig(f'./figures/{size}.png')