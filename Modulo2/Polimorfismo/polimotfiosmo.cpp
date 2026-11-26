

#include<iostream>
#include<string>


using namespace std;


class Figura {
public:
    virtual double area() {
        return 0;
    }
};


class Rectangulo : public Figura {
    double b, h;
public:
    Rectangulo(double x, double y) { b = x; h = y; }

    double area() override {
        return b * h;
    }
};


class Circulo : public Figura {
    double r;
public:
    Circulo(double y) {r = y; }

    double area() override {
        return 3.14 *r * r;
    }
};

void informe(Figura& f) {
    cout << "Area: " << f.area() << endl;
}


int main(){
    Rectangulo r(3, 4);
    Circulo c(2);
    informe(r);   // Area: 12
    informe(c);
    
}
