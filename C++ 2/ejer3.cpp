//devolver solo la parte de fraccion de un numero
#include <iostream>
using namespace std;
int main() {
    double number;
    cout << "Ingrese un numero: ";
    cin >> number;

    // Obtener la parte fraccionaria
    double fractionalPart = number - static_cast<int>(number); // Restar la parte entera del número para obtener la parte fraccionaria

    // Mostrar la parte fraccionaria
    cout << "La parte fraccionaria de " << number << " es: " << fractionalPart << endl;

    return 0;
}