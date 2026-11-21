#include<iostream>
#include<string>
using namespace std;

class Estudiante{
private:
    string nombre;
    double nota;
public:

    Estudiante(string nom, double n){
        nombre = nom;
        nota = n;
    }
    
    string getNombre(){
        return nombre;
    }
    double getNota(){
        return nota;
    }

    void setNota(double n){
        if(n>100 || n < 0 ){
            cout<< "Nota invalida"<< endl;
        }else{
            nota =  n;
        }
    }

};

int main(){
    Estudiante maria("maria", 90.2);

    cout << maria.getNota()<< endl;

    maria.setNota(45);

    cout << maria.getNota()<< endl;


    return 0;
}