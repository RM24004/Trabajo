//elementos positivos negativos y ceros de un vector
#include <iostream>
using namespace std;

int main() {
    const int SIZE = 5; // Puedes cambiar este valor para un tamaño diferente
    int vector[SIZE];
    int positivos = 0;
    int negativos = 0;
    int ceros = 0;

    cout << "Ingrese los elementos del vector:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> vector[i];
        if (vector[i] > 0) {
            positivos++;
        } else if (vector[i] < 0) {
            negativos++;
        } else {
            ceros++;
        }
    }

    cout << "\nElementos positivos: " << positivos << endl;
    cout << "Elementos negativos: " << negativos << endl;
    cout << "Elementos ceros: " << ceros << endl;

    return 0;
}