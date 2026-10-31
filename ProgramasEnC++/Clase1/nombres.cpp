#include <iostream>
#include <string>
using namespace std;
int main(){
    string nombre;
    //cin >> nombre;
    getline(cin, nombre);
    cout << nombre;
    
    return 0;
}