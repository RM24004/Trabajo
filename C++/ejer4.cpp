//vector voltajes sumarlos y mostrar su promedio si pasa del valor de 220 si no correcto
#include <iostream>
using namespace std;
int main() {
    const int SIZE = 5; // Puedes cambiar este valor para un tamaño diferente
    double voltajes[SIZE];
    double suma = 0.0;
    double promedio;

    cout << "Ingrese los voltajes:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> voltajes[i];
        suma += voltajes[i];
    }

    promedio = suma / SIZE;

    cout << "\nPromedio de voltajes: " << promedio << endl;
    cout << "Suma de voltajes: " << suma << endl;
    if (promedio > 220) {
        cout << "El promedio supera el valor de 220." << endl;
    } else {
        cout << "El promedio es correcto." << endl;
    }

    return 0;
}