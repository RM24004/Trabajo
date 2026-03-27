//rellenar un array de 10 numeros y con punteros mostrar cuales son pares e impares y su ubicacion en memoria
#include <iostream>
using namespace std;
int main() {
    const int SIZE = 10;
    int arr[SIZE];
    int *ptr = arr; //puntero que apunta al primer elemento del array

    cout << "Ingrese " << SIZE << " numeros:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> arr[i];
    }

    cout << "Numeros pares e impares con su ubicacion en memoria:" << endl;
    for (int i = 0; i < SIZE; i++) {
        if (arr[i] % 2 == 0) {
            cout << "El numero " << arr[i] << " es par. ";
        } else {
            cout << "El numero " << arr[i] << " es impar. ";
        }
        cout << "Direccion de memoria: " << (ptr + i) << endl; //muestra la direccion de memoria del elemento actual
    }

    return 0;
}