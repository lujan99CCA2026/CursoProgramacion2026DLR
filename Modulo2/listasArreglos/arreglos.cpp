

#include <iostream>

using namespace std;


int main(){

    int notas[3] = {70, 85, 90};
 
    cout << notas[0] << endl;  // 70
    cout << notas[1] << endl;
    notas[1] = 95;
    cout << notas[1] << endl;  // 95

    return 0;
}