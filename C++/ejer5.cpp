// suma de los elemntos de una matiz 6x6 en diagonal 
#include <iostream>
using namespace std;
int main() {
    const int SIZE = 3;
    int matriz[SIZE][SIZE];
    int sumaDiagonalPrincipal = 0;
  
    std::cout << "Ingrese los elementos de la matriz:" << std::endl;

    for (int i = 0; i < SIZE; i++) { // Recorre las filas
        for (int j = 0; j < SIZE; j++) { // Recorre las columnas
            cin >> matriz[i][j]; // Lee el elemento de la matriz
        }
    }

    // Suma de la diagonal principal
    for (int i = 0; i < SIZE; i++) { // Recorre las filas para sumar los elementos de la diagonal principal
        sumaDiagonalPrincipal += matriz[i][i]; // Suma el elemento de la diagonal principal (donde fila y columna son iguales)
    }

    std::cout << "\nSuma de la diagonal principal: " << sumaDiagonalPrincipal << std::endl;
   
    return 0;
}