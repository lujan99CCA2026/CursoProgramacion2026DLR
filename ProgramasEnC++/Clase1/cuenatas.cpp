// cuentas.cpp · dos enteros: su suma, resta y producto

#include <iostream>

using namespace std;

int main(){

    int num1, num2, suma, resta, procucto;

    cout << "Introduzca su primer numero:"<<endl;
    cin >> num1;
    cout << "Introduzca su segundo numero: "<<endl;
    cin >> num2;
    suma = num1 + num2;
    resta = num1 - num2;
    procucto = num1 * num2;
    cout << "La suma es: "<< suma<< endl;
    cout << "La resta es: "<< resta << endl;
    cout << "El producto es: "<< procucto << endl;

    return 0;
}