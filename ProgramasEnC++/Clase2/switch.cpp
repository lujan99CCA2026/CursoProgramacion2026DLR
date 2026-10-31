#include <iostream>
using namespace std;

int main(){
    int dia;
    cout << "introduzca un dia de la semana de 1-7"<< endl;
    cin >> dia;
    switch (dia){
    case 1:
        cout << "Es lunes"<< endl;
        break;
    case 2:
        cout << "Es martes"<< endl;
        break;
    case 3:
        cout << "Es miercoles"<< endl;
        break;
    case 4:
        cout << "Es jueves"<< endl;
        break;
    default:
        cout << "Esa opcion no esta disponible"<< endl;
        break;
    }
    
    return 0;

}