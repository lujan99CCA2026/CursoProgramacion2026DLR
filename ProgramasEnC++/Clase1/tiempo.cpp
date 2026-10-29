// tiempo.cpp · segundos a horas, minutos y segundos


#include <iostream>
using namespace std;

int main(){
    int totalsegundos;
    cout<< "Introduce todos los segundos que quiere convertir:"<< endl;
    cin >> totalsegundos;
    //3600 segundos = 1hora
    int horas = totalsegundos/3600;
    int residuo = totalsegundos%3600;

    
    int minutos = residuo / 60;
    int segundos = residuo % 60;

    cout <<"Tienes horas:"<< horas<< endl;
    cout << "Tienens minutos"<< minutos << endl ;
    cout << "Tienens segundos"<< segundos << endl;

    
    return 0;
}