#include <iostream>
using namespace std;

int main(){
    int clave;
    do {
        cout << "Clave: ";
        cin >> clave;
    } while (clave != 1234);

    cout << "Ingresaste"<< endl;
    return 0;
}