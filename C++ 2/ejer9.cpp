//sin usar pow calcular la potencia de un numero dado una base y un exponente
#include <iostream>
using namespace std;
int main() {
    double base;
    int exponent;

    cout << "Ingrese la base: ";
    cin >> base;
    cout << "Ingrese el exponente: ";
    cin >> exponent;

    double result = 1; // Inicializar el resultado a 1

    // Calcular la potencia utilizando un bucle
    for (int i = 0; i < exponent; i++) {
        result *= base; // Multiplicar la base por sí misma 'exponent' veces
    }

    cout << base << " elevado a " << exponent << " es: " << result << endl;

    return 0;
}
