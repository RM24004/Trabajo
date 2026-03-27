// funcion recursiva para calcular la potencia de un numero dado una base y un exponente
#include <iostream>
using namespace std;
double potencia(double base, int exponent) {
    if (exponent == 0) {
        return 1; // Cualquier número elevado a la potencia de 0 es 1
    } else if (exponent < 0) {
        return 1 / potencia(base, -exponent); // Manejar exponentes negativos
    } else {
        return base * potencia(base, exponent - 1); // Llamada recursiva
    }
}
int main() {
    double base;
    int exponent;

    cout << "Ingrese la base: ";
    cin >> base;
    cout << "Ingrese el exponente: ";
    cin >> exponent;

    double result = potencia(base, exponent);

    cout << base << " elevado a " << exponent << " es: " << result << endl;

    return 0;
}
