#include <iostream>
#include <ctime>

//Calcula el N esimo numero de fibonacci
int fibonacci(int N){
  if(N==0 || N==1){
    return N;
  }
  else{
    return fibonacci(N-2)+fibonacci(N-1);
  }
}

//Calcula el tiempo que se demora en calcular fibonacci(N)
float get_time(int N){
  clock_t t;
  t = clock();
  fibonacci(N);
  t = clock() -t;
  float time = ((float)t)/CLOCKS_PER_SEC;
  return time;
}

//Imprime N y el tiempo en calcular fibonacci(N)
int main(){
  for(int i = 0;i<40;i++){
    float tiempo = get_time(i);
    std::cout<<i << "," << tiempo<<std::endl;
  }
}
