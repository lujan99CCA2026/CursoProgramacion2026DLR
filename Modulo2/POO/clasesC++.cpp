#include<iostream>
#include<string>
#include<vector>

using namespace std;



class Estudiante {
public:
    string nombre;
    double nota;
 
    Estudiante(string n, double x) {
        nombre = n;
        nota = x;
    }
 
    bool aprobo() {
        return nota >= 61;
    }
};

class Producto{

    
public:
    string nombre;
    double precio;
    int cantidad;
    Producto(string n, double a, int b){
        nombre = n;
        precio = a;
        cantidad = b;
    }

    void mostrar(){
        cout << nombre << "Precio:" << precio << "Cantidad:"<< cantidad <<endl;
    }

    bool vender(int cantidads){
        if(cantidads > cantidad){
            return false;
        }else{
            cantidad = cantidad - cantidads;
            return true;
        }

    }

};

int main(){

    Producto arroz("arroz", 10.0, 45);
    arroz.mostrar();

    if(arroz.vender(10)){
        cout<< "Si alcanzo"<< endl;
    }else{
        cout<<"No alcanzo"<< endl;
    }
    arroz.mostrar();
    Estudiante ana("Ana", 85);
    Estudiante luis("Luis", 58);
 
    cout << ana.nombre << endl;      // Ana
    luis.nota = 63;
    if (luis.aprobo()) {
        cout << "Luis aprobo" << endl;
    }
 
    vector<Estudiante> curso = {ana, luis};
    for (Estudiante e : curso) {
        cout << e.nombre << ": " << e.nota << endl;
    }

    return 0;
}
