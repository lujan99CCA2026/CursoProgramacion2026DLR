#include <iostream>
#include <vector>
using namespace std;
 
int main() {
    vector<int> notas = {70, 85, 90};
    notas.push_back(64);
    cout << notas[3] << endl;       // 64
    cout << notas.size() << endl;  // 4
    return 0;
}