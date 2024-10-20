from datetime import datetime 
import time
import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass
    def exposed_get_answer(self): 
        return 42

    exposed_the_real_answer_though = 43 

    def get_question(self): 
        return "Qual é a cor do cavalo branco de Napoleão?"
    
    def exposed_vector_sum(self, vector):
        start = time.time() 

        sum = 0
        for value in vector:
            sum += value

        end = time.time()

        start_time = datetime.fromtimestamp(start)
        end_time = datetime.fromtimestamp(end)

        return (f"Start: {start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}, End: {end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
    
    def exposed_get_procedure_time(self):
        return 

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=4200)
    t.start()
