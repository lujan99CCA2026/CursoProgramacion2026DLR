// Pidan 3 notas con cin, guárdenlas con push_back y muestren el promedio.

#include <iostream>
#include <vector>
using namespace std;


int main(){
vector<int> notas = {};
    for( int i = 0 ; i < 3; i++ ){
        int nota;
        cout << "ingrese la nota"<< i<< endl;
        cin >>nota; 
        notas.push_back(nota);

    }
    int suma  = 0;
    for(int f = 0 ; f < notas.size(); f++){
        suma = suma + notas[f];

    }
    cout << suma<<endl;
    cout << suma/notas.size();

   

    return 0;
}