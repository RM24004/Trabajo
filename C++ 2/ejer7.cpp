//crear una funcion que calcule una division enterea y el resto utilizando restos sucesivos
#include <iostream>
using namespace std;
void divisionEntera(int dividend, int divisor, int &quotient, int &remainder) {
    quotient = 0; // Inicializar el cociente
    remainder = dividend; // Inicializar el resto con el dividendo

    while (remainder >= divisor) {
        remainder -= divisor; // Restar el divisor del resto
        quotient++; // Incrementar el cociente
    }
}
int main() {
    int dividend, divisor, quotient, remainder;

    cout << "Ingrese el dividendo: ";
    cin >> dividend;
    cout << "Ingrese el divisor: ";
    cin >> divisor;

    if (divisor == 0) {
        cout << "Error: El divisor no puede ser cero." << endl;
        return 1; // Salir con error
    }

    divisionEntera(dividend, divisor, quotient, remainder);

    cout << "Cociente: " << quotient << endl;
    cout << "Resto: " << remainder << endl;

    return 0;
}