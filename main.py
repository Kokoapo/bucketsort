import matplotlib.pyplot as plt
from execute import execute

sizes = [100000, 500000, 1000000]
buckets = [100, 1000, 10000, 100000]

for size in sizes:
    times = []
    for bucket in buckets:
        final_time = execute(size, bucket)
        times.append(final_time)
        print(f'Tamanho {size} Baldes {bucket} Tempo {final_time}')
    plt.close()
    plt.plot(buckets, times)

    plt.xscale('log')

    plt.xlabel('Número de Baldes')
    plt.ylabel('Tempo (Segundos)')
    plt.title(f'Execução para {size} Elementos')

    plt.savefig(f'./figures/{size}.png')