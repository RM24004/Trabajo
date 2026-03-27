//pedirle al usuario rellenar un array y con punteros mostrar el valor menor y su ubicacion en memoria
#include <iostream>
using namespace std;
int main() {
    int SIZE;
    cout << "Ingrese el tamaño del array: ";
    cin >> SIZE;
    int arr[SIZE];
    int *ptr = arr; //puntero que apunta al primer elemento del array

    cout << "Ingrese " << SIZE << " numeros:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> arr[i];
    }

    int menor = arr[0];
    int *ptrMenor = ptr; //puntero que apunta al elemento menor

    for (int i = 1; i < SIZE; i++) {
        if (arr[i] < menor) {
            menor = arr[i];
            ptrMenor = ptr + i; //actualiza el puntero para que apunte al nuevo elemento menor
        }
    }

    cout << "El numero menor es: " << menor << endl;
    cout << "Direccion de memoria del numero menor: " << ptrMenor << endl;

    return 0;
}