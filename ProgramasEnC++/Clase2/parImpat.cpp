// Hacer un programa que reconozca cuando un numero es par o impar

#include <iostream>

using namespace std;

int main(){
    int numero;
    cout << "Ingrese un numero";
    cin >> numero;
    if (numero % 2 == 0 ){
        cout<< "Es par"<< endl;
        cout<< numero % 2 << endl;
    }else{
        cout<< "Es impar"<< endl;
        cout<< numero % 2 << endl;
    }



    return 0;
}