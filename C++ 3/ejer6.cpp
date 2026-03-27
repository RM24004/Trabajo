//crear una funcion para almacenar n numeros en un array dinamico y otra funcion para buscar el numero ingresado por el usuario
#include <iostream>
using namespace std;
void almacenarNumeros(int *&arr, int &size) {
    cout << "Ingrese el tamaño del array: ";
    cin >> size;
    arr = new int[size]; //crear un array dinámico

    cout << "Ingrese " << size << " numeros:" << endl;
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }
}
bool buscarNumero(int *arr, int size, int num) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == num) {
            return true; //numero encontrado
        }
    }
    return false; //numero no encontrado
}
int main() {
    int *arr = nullptr; //puntero para el array dinámico
    int size;
    almacenarNumeros(arr, size); //llamar a la función para almacenar números

    int num;
    cout << "Ingrese un numero para buscar: ";
    cin >> num;

    if (buscarNumero(arr, size, num)) {
        cout << "El numero " << num << " fue encontrado en el array." << endl;
    } else {
        cout << "El numero " << num << " no fue encontrado en el array." << endl;
    }

    delete[] arr; //liberar la memoria del array dinámico
    return 0;
}