//pedir al usuario numeros, rellenar un array y ordenarlos ascendentemente
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

    //ordenar el array ascendentemente usando el puntero
    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = 0; j < SIZE - i - 1; j++) {
            if (*(ptr + j) > *(ptr + j + 1)) {
                //intercambiar los elementos
                int temp = *(ptr + j);
                *(ptr + j) = *(ptr + j + 1);
                *(ptr + j + 1) = temp;
            }
        }
    }

    cout << "Array ordenado ascendentemente:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << *(ptr + i) << " "; //muestra el valor del elemento actual
    }
    cout << endl;

    return 0;
}
