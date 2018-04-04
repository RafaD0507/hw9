cpp_vs_python.png : times_python.csv times_cpp.csv
	python RafaelSanabria_Graficas.py

times_python.csv :
	python RafaelSanabria_GenerarTiempos.py > times_python.csv

times_cpp.csv: gen_times.x
	./gen_times.x > times_cpp.csv

gen_times.x :
	c++ RafaelSanabria_GenerarTiempos.cpp -o gen_times.x

clean:
	times_cpp.csv times_python.csv gen_times.x
