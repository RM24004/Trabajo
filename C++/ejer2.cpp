//suma resta division multiplicacion media aritmetica de todos los elementos de un vector 
#include <iostream>
using namespace std;

int main() {
    const int SIZE = 5;
    int vector[SIZE];
    int suma = 0;
    int resta = 0;
    int multiplicacion = 1;
    double mediaAritmetica;

    string encabezados[4] = {"Suma", "Resta", "Multiplicacion", "Media Aritmetica"};
    double resultados[4];

    cout << "Ingrese los elementos del vector:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> vector[i];
        suma += vector[i];
        resta -= vector[i];
        multiplicacion *= vector[i];
    }

    mediaAritmetica = static_cast<double>(suma) / SIZE;
    // Guardar resultados en el vector
    resultados[0] = suma;
    resultados[1] = resta;
    resultados[2] = multiplicacion;
    resultados[3] = mediaAritmetica;

    cout << endl;
    // Mostrar encabezados y resultados
    for (int i = 0; i < 4; i++) {
        cout << encabezados[i] << ": " << resultados[i] << endl;
    }
    
    return 0;
}