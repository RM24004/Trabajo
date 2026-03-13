//usando una matriz y un vector contar la cantidad de numeros primos 
#include <iostream>
using namespace std;
bool esPrimo(int numero) {
    if (numero <= 1) return false; // Los números menores o iguales a 1 no son primos
    for (int i = 2; i <= numero / 2; i++) {
        if (numero % i == 0) return false; // Si el número es divisible por algún número entre 2 y su mitad, no es primo
    }
    return true; // Si no es divisible por ningún número, es primo
}

int main() {
    const int SIZE = 5; // Puedes cambiar este valor para un tamaño diferente
    int matriz[SIZE][SIZE];
    int vector[SIZE];
    int contadorPrimos = 0;

    cout << "Ingrese los elementos de la matriz:" << endl;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            cin >> matriz[i][j];
            if (esPrimo(matriz[i][j])) {
                contadorPrimos++;
            }
        }
    }

    cout << "Ingrese los elementos del vector:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> vector[i];
        if (esPrimo(vector[i])) {
            contadorPrimos++;
        }
    }

    cout << "\nCantidad de números primos en la matriz y el vector: " << contadorPrimos << endl;

    return 0;
}