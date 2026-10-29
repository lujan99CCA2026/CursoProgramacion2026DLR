// promedio.cpp · tres notas y su promedio (¡ojo con la división!)

#include <iostream>

using namespace std;

int main(){
    int nota1, nota2, nota3;
    double promedio;
    cout << "Nota 1:"<< endl;
    cin >> nota1;
    cout << "Nota 2:"<< endl;
    cin >> nota2;
    cout << "Nota 3:"<< endl;
    cin >> nota3;

    promedio = (nota1 + nota2 + nota3)/3;

    cout << "El promedio de las tres notas es: "<< promedio << endl ;




    return 0;
}