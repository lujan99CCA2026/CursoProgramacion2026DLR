
#include <iostream>

using namespace std;

int main(){
    int nota;
    cout << "ingrese una nota"<< endl;
    cin >> nota;
    if(nota >= 90){
        cout << "exelente";
    }else if( nota >=61){
        cout << "La nota es de aprobado"<< endl;
    }else {
        cout << "Reprobado"<< endl;
    }
    return 0;
}