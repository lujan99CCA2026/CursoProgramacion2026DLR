#include<iostream>

using namespace std;

// int cuadrado(int n) · devolver n × n
int cuadrado(int n){
    return n*n;
}
// void saludar(string nombre) · mostrar un saludo

void saludar(string nombre){
    cout<< "Hola, "<< nombre << endl;
}
// bool es_par(int n) · usarla dentro de un if

bool es_par(int n){
    return (n%2==0);
}
// double area_circulo(double r) · devolver 3.1416 × r × r

double area_circulo(double r){
    return 3.1416*r*r;
}
int main(){
    // int p = cuadrado(2);
    // cout<< p<< endl;

    //saludar("David");
    // bool resultado = es_par(21);
    // cout<< resultado << endl;


    double resultadoCirculo = area_circulo(9);
    cout << resultadoCirculo << endl;
    return 0;
}