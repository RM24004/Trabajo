//solicitar al usuario una matriz dinamica y crear su matriz transpuesta
#include <iostream>
using namespace std;
void crearMatriz(int **&matriz, int filas, int columnas) {
    matriz = new int*[filas]; //crear un array de punteros para las filas
    for (int i = 0; i < filas; i++) {
        matriz[i] = new int[columnas]; //crear un array para cada fila
    }

    cout << "Ingrese los elementos de la matriz:" << endl;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cin >> matriz[i][j];
        }
    }
}
void transponerMatriz(int **matriz, int **&matrizTranspuesta, int filas, int columnas) {
    matrizTranspuesta = new int*[columnas]; //crear un array de punteros para las filas de la matriz transpuesta
    for (int i = 0; i < columnas; i++) {
        matrizTranspuesta[i] = new int[filas]; //crear un array para cada fila de la matriz transpuesta
    }

    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            matrizTranspuesta[j][i] = matriz[i][j];
        }
    }
}
int main() {
    int filas, columnas;
    cout << "Ingrese el numero de filas: ";
    cin >> filas;
    cout << "Ingrese el numero de columnas: ";
    cin >> columnas;

    int **matriz = nullptr; //puntero para la matriz original
    int **matrizTranspuesta = nullptr; //puntero para la matriz transpuesta

    crearMatriz(matriz, filas, columnas); //crear la matriz original
    transponerMatriz(matriz, matrizTranspuesta, filas, columnas); //crear la matriz transpuesta

    // Mostrar la matriz transpuesta
    cout << "La matriz transpuesta es:" << endl;
    for (int i = 0; i < columnas; i++) {
        for (int j = 0; j < filas; j++) {
            cout << matrizTranspuesta[i][j] << " ";
        }
        cout << endl;
    }
    // Liberar memoria
    for (int i = 0; i < filas; i++) {
        delete[] matriz[i];
    }
    delete[] matriz;
    for (int i = 0; i < columnas; i++) {
        delete[] matrizTranspuesta[i];
    }
    delete[] matrizTranspuesta;
    return 0;
}
