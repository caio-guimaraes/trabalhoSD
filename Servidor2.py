import rpyc
import random

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass

    def on_disconnect(self, conn):
        #  código que é executado quando uma conexão é finalizada, caso seja necessário
        pass

    def exposed_sum_list(self, tam):
        list = self.get_list(tam)
        print(list)
        sum = 0
        for i in range(0, tam):
            sum += list[i]
        return sum

    def get_list(self, tam):
        print(tam)
        list = tam * [0]
        for i in range(0, tam):
            list[i] = random.randint(0, tam-1)
        return list


# Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(MyService, port=18861)
    t.start()
