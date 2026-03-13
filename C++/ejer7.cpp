//calculo de un producto escalar de un vector
#include <iostream>
using namespace std;
int main() {
    const int SIZE = 5; // Puedes cambiar este valor para un tamaño diferente
    int vector1[SIZE];
    int vector2[SIZE];
    int productoEscalar = 0;

    cout << "Ingrese los elementos del primer vector:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> vector1[i];
    }

    cout << "Ingrese los elementos del segundo vector:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> vector2[i];
    }

    // Calcular el producto escalar
    for (int i = 0; i < SIZE; i++) {
        productoEscalar += vector1[i] * vector2[i]; // Multiplica los elementos correspondientes de los dos vectores y los suma al producto escalar
    }

    cout << "\nEl producto escalar de los dos vectores es: " << productoEscalar << endl;

    return 0;
}