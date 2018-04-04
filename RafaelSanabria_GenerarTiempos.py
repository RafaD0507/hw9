import time

def fibonacci(N):
    #Retorna el N esimo numero de Fibonacci
    if(N== 0 or N==1):
        return N
    else:
        return fibonacci(N-2)+fibonacci(N-1)

def get_time(N):
    #Retorna el tiempo que se demora en calcular el N esimo numero de fibonacci
    t0 = time.time()
    fibonacci(N)
    t1 = time.time() - t0
    return t1

#N y el tiempo que se demora en calcular fibonacci(N)
for i in range(36):
    print str(i) + "," + str(get_time(i))
