//fecha actual y calculo de la edad de un usuario
#include <iostream>
#include <string>
#include <ctime>
using namespace std;
int main() {
    //obtener el nombre del usuario
    string name;
    cout << "Ingrese su nombre: ";
    getline(cin, name);

    // Obtener la fecha actual
    time_t now = time(0);
    tm * ltm = localtime(&now);
    int currentYear = 1900 + ltm->tm_year;

    // Solicitar al usuario su año de nacimiento
    int birthYear;
    cout << "Ingrese su anio de nacimiento: ";
    cin >> birthYear;

    // Calcular la edad
    int age = currentYear - birthYear;

    // Mostrar la edad al usuario
    cout << "Hola, " << name << "!" << endl;
    cout << "Su edad es: " << age << " anios." << endl;

    return 0;
}