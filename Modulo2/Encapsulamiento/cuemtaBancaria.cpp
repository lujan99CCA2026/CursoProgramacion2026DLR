#include<iostream>

using namespace std;

class CuentaBancaria {
private:
    string titular;
    double saldo;
 
public:
    CuentaBancaria(string t, double s) {
        titular = t;
        saldo = s;
    }
    double getSaldo() {
        return saldo;
    }
    void depositar(double monto) {
    if (monto > 0) {
        saldo = saldo + monto;
    }
}
    bool retirar(double monto) {
    if (monto > 0 && monto <= saldo) {
        saldo = saldo - monto;
        return true;
    }
    return false;
}
};

int main(){


    return 0;
}