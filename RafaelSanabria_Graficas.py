import matplotlib.pyplot as plt
import numpy as np

#Carga los datos de los archivos de texto
datosPY = np.loadtxt("times_python.csv", delimiter=",")
datosCPP = np.loadtxt("times_cpp.csv", delimiter=",")

#Grafica los datos
plt.figure()
plt.plot(datosPY[:,0],datosPY[:,1], label="Python")
plt.plot(datosCPP[:,0],datosCPP[:,1], label="C++")
plt.xlabel('N')
plt.ylabel('Tiempo en segundos')
plt.legend()
plt.title('C++ vs Python para calcular el Nesimo numero de Fibonacci')
plt.savefig("cpp_vs_python.png")
plt.close()

