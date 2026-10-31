#include <iostream>
using namespace std;

int main(){
    int suma = 0, num;
    for (int i = 1; i <= 10; i++) {
        cout <<"ingrese numer"<< i << endl;
        cin>> num;
        suma = suma + num;

    }

    cout << "La suma total fue de"<< suma;

    return 0;
}