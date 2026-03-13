//matrices 5x5
#include <iostream>
using namespace std;

int main() {
    const int SIZE = 5;
    int matriz[SIZE][SIZE];
    int sumaFilas[SIZE] = {0};
    int sumaColumnas[SIZE] = {0};

    cout << "Ingrese los elementos de la matriz:" << endl;

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            cin >> matriz[i][j];
        }
    }

    // Suma de filas
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            sumaFilas[i] += matriz[i][j];
        }
    }

    // Suma de columnas
    for (int j = 0; j < SIZE; j++) {
        for (int i = 0; i < SIZE; i++) {
            sumaColumnas[j] += matriz[i][j];
        }
    }

    cout << "\nSuma de filas:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << sumaFilas[i] << " ";
    }

    cout << "\nSuma de columnas:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << sumaColumnas[i] << " ";
    }

    return 0;
}