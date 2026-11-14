#include <iostream>
#include <map>
#include <string>
using namespace std;
 
int main() {
    //Definimos el diccionario
    map<string, int> stock;
    // Agregando valores al diccionario
    stock["pan"] = 40;
    stock["leche"] = 12;
    // Como se lee el diccionario 
    for (auto par : stock)
        cout << par.first << ": " << par.second << endl;
    return 0;
}