//ordenar vector de mayor a menor
#include <iostream>
using namespace std;
int main() {
    const int SIZE = 5; // Puedes cambiar este valor para un tamaño diferente
    int vector[SIZE];

    cout << "Ingrese los elementos del vector:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> vector[i];
    }

    // Ordenar el vector de mayor a menor usando el algoritmo de burbuja
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = 0; j < SIZE - i - 1; j++) {
            if (vector[j] < vector[j + 1]) { // Cambia a '>' para ordenar de menor a mayor
                swap(vector[j], vector[j + 1]); // Intercambia los elementos
            }
        }
    }

    cout << "\nVector ordenado de mayor a menor:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << vector[i] << " ";
    }
    cout << endl;

    return 0;
}