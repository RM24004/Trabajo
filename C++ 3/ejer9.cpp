//suma de 2 matrices dinamicas
#include <iostream>
using namespace std;
void sumarMatrices(int **matrizA, int **matrizB, int **matrizSuma, int filas, int columnas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            matrizSuma[i][j] = matrizA[i][j] + matrizB[i][j]; //suma elemento a elemento
        }
    }
}
int main() {
    int filas, columnas;
    cout << "Ingrese el numero de filas: ";
    cin >> filas;
    cout << "Ingrese el numero de columnas: ";
    cin >> columnas;

    // Crear matrices dinámicas
    int **matrizA = new int*[filas];
    int **matrizB = new int*[filas];
    int **matrizSuma = new int*[filas];
    for (int i = 0; i < filas; i++) {
        matrizA[i] = new int[columnas];
        matrizB[i] = new int[columnas];
        matrizSuma[i] = new int[columnas];
    }

    // Rellenar matriz A
    cout << "Ingrese los elementos de la matriz A:" << endl;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cin >> matrizA[i][j];
        }
    }

    // Rellenar matriz B
    cout << "Ingrese los elementos de la matriz B:" << endl;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cin >> matrizB[i][j];
        }
    }

    // Sumar las matrices
    sumarMatrices(matrizA, matrizB, matrizSuma, filas, columnas);

    // Mostrar la matriz suma
    cout << "La suma de las matrices A y B es:" << endl;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cout << matrizSuma[i][j] << " ";
        }
        cout << endl;
    }

    // Liberar memoria
    for (int i = 0; i < filas; i++) {
        delete[] matrizA[i];
        delete[] matrizB[i];
        delete[] matrizSuma[i];
    }
    delete[] matrizA;
    delete[] matrizB;
    delete[] matrizSuma;

    return 0;
}