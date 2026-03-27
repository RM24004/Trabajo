//verificar si es par o impar y ver su ubicacion en memoria con un puntero
#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Ingrese un numero: ";
    cin >> num;

    int *ptr = &num; //puntero que almacena la dirección de memoria de num

    if (num % 2 == 0) {
        cout << "El numero " << num << " es par." << endl;
    } else {
        cout << "El numero " << num << " es impar." << endl;
    }

    cout << "La direccion de memoria del numero es: " << ptr << endl;

    return 0;
}