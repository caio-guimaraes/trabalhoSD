import time
import rpyc
import sys


def ler_tamanho_vetor():
    tamanho = input("Digite o tamanho do vetor: ")
    print(tamanho)
    return int(tamanho)



if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server, 18861)

n = ler_tamanho_vetor()
start = time.time()
print(conn.root.sum_list(n))
end = time.time()
print(end-start)