#include <iostream>

using namespace std;

int doble(int n){
    return n * 2; 
}

void line(){
    cout << "--------------------------------"<< endl;
}

int main(){
    cout << "INgrese un numero"<< endl;
    int n;
    cin >> n ;
    int p = doble(n);
    cout << p<< endl;
    line();

    return 0;
}


