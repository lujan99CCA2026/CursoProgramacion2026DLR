

#include<iostream>
#include<string>


using namespace std;

class Persona {
protected:
    string nombre;
    int edad;
    Persona(string n, int ed) { 
        nombre = n; 
        edad = ed;
    }
public:
    void presentarse() {
        cout << "Soy " << nombre <<" Y tengo: "<< edad<<endl; 
    }
};
 
class Estudiante : public Persona {
public:
    string carrera;
    Estudiante(string n, int ed, string c) : Persona(n, ed) {
        carrera = c;
    }
};

class Docente : public Persona {
public: 
    string materia;
    Docente(string n, int ed, string m): Persona(n, ed){
        materia = m; 
    }

    void dictar(){
        cout << nombre << " dicta la materia de: "<< materia ;
    }

};


int main(){

    Estudiante e("Ana", 22,"Sistemas");
    e.presentarse();
    

    Docente d("raul", 55, "programacion");
    d.presentarse();
    d.dictar();
    return 0;
}
