//determinar si un numero es primo o no y ver su ubicacion en memoria con un puntero
#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Ingrese un numero: ";
    cin >> num;

    int *ptr = &num; //puntero que almacena la dirección de memoria de num

    bool esPrimo = true;
    if (num <= 1) {
        esPrimo = false;
    } else {
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                esPrimo = false;
                break;
            }
        }
    }

    if (esPrimo) {
        cout << "El numero " << num << " es primo." << endl;
    } else {
        cout << "El numero " << num << " no es primo." << endl;
    }

    cout << "La direccion de memoria del numero es: " << ptr << endl;

    return 0;
}