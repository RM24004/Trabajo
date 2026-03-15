//suma resta division multiplicacion media aritmetica de todos los elementos de un vector 
#include <iostream>
using namespace std;

int main() {
    const int SIZE = 3;
    int vector[SIZE];
    int suma = 0;
    int resta = 0;
    int multiplicacion = 1;
    double division = 1.0;
    double mediaAritmetica;

    string encabezados[5] = {"Suma", "Resta", "Multiplicacion", "Division", "Media Aritmetica"};
    double resultados[5];

    cout << "Ingrese los elementos del vector:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> vector[i];
        suma += vector[i];
        multiplicacion *= vector[i];
        if (i == 0) {
            resta = vector[i];
            division = vector[i];
        } else {
            resta -= vector[i];
            division /= vector[i];
        }
        
        
    }

    mediaAritmetica = static_cast<double>(suma) / SIZE;
    // Guardar resultados en el vector
    resultados[0] = suma;
    resultados[1] = resta;
    resultados[2] = multiplicacion;
    resultados[3] = division;
    resultados[4] = mediaAritmetica;

    cout << endl;
    // Mostrar encabezados y resultados
    for (int i = 0; i < 5; i++) {
        cout << encabezados[i] << ": " << resultados[i] << endl;
    }
    
    return 0;
}