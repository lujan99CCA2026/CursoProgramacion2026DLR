#include <iostream>
#include <vector>
using namespace std;
 
int main() {
    vector<int> edades = {7, 5, 18, 22, 34, 23, 54, 65};
    for(int i = 0; i< edades.size() ; i++){
        cout << i << "=" << edades[i]<< endl;
    }
    return 0;
}