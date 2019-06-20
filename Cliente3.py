import rpyc
import sys


def ler_tamanho_vetor():
    tamanho = input("Digite o tamanho do vetor: ")
    print(tamanho)
    return int(tamanho)


def f(x):
    return x**2

# if len(sys.argv) < 2:
#     exit("Usage {} SERVER".format(sys.argv[0]))

# server = sys.argv[1]
server = "localhost"

conn = rpyc.connect(server, 18861)

n = ler_tamanho_vetor()

print(conn.root.sum_list(n))
