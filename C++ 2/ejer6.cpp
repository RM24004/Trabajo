//calculular los cuadrados de los enteros del 1 al 10 y mostrar el resultado
#include <iostream>
using namespace std;
int main() {
    cout << "Cuadrados de los enteros del 1 al 10:" << endl;
    for (int i = 1; i <= 10; i++) {
        cout << "El cuadrado de " << i << " es: " << i * i << endl;
    }
    return 0;
}