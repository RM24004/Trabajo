//calcular areas de figuras geometricas cuadrado, rectangulo, triangulo y circulo
#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int choice;
    cout << "Seleccione la figura geometrica para calcular su area:" << endl;
    cout << "1. Cuadrado" << endl;
    cout << "2. Rectangulo" << endl;
    cout << "3. Triangulo" << endl;
    cout << "4. Circulo" << endl;
    cout << "Ingrese su opcion (1-4): ";
    cin >> choice;

    switch (choice) {
        case 1: {
            double side;
            cout << "Ingrese el lado del cuadrado: ";
            cin >> side;
            double area = side * side;
            cout << "El area del cuadrado es: " << area << endl;
            break;
        }
        case 2: {
            double length, width;
            cout << "Ingrese la longitud del rectangulo: ";
            cin >> length;
            cout << "Ingrese el ancho del rectangulo: ";
            cin >> width;
            double area = length * width;
            cout << "El area del rectangulo es: " << area << endl;
            break;
        }
        case 3: {
            double base, height;
            cout << "Ingrese la base del triangulo: ";
            cin >> base;
            cout << "Ingrese la altura del triangulo: ";
            cin >> height;
            double area = (base * height) / 2;
            cout << "El area del triangulo es: " << area << endl;
            break;
        }
        case 4: {
            double radius;
            cout << "Ingrese el radio del circulo: ";
            cin >> radius;
            double area = M_PI * radius * radius; // M_PI es una constante de cmath que representa el valor de pi
            cout << "El area del circulo es: " << area << endl;
            break;
        }
        default:
            cout << "Opcion invalida. Por favor seleccione una opcion entre 1 y 4." << endl;
    }

    return 0;
}
