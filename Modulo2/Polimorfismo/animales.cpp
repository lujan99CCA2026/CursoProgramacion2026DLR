
#include<iostream>
#include<string>
using namespace std;


class Animal{

public: 
    virtual void hablar(){
        cout<< "..."<< endl;
    }

};

class Perro: public Animal{
    void hablar() override{
        cout << "Guau Guau"<< endl;
    }
};

class Gato: public Animal{
    void hablar() override{
        cout << "Miai Miau"<< endl;
    }
};


void hacerHablar(Animal& a){
    a.hablar();
}

int main(){


    Perro a;
    Gato j;
    // hacerHablar(a);
    hacerHablar(j);

    return 0;
}
