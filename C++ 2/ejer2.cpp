//datos de personas nombre, edad, peso, altura y mostrar la peso con menor edad, el promedio de peso y el promedio de altura
#include <iostream>
#include <string>
using namespace std;
int main() {
    const int SIZE = 5;
    string names[SIZE];
    int ages[SIZE];
    float weights[SIZE];
    float heights[SIZE];

    // Ingresar datos de las personas
    for (int i = 0; i < SIZE; i++) {
        cout << "Ingrese el nombre de la persona " << i + 1 << ": ";
        getline(cin, names[i]);
        cout << "Ingrese la edad de " << names[i] << ": ";
        cin >> ages[i];
        cout << "Ingrese el peso de " << names[i] << ": ";
        cin >> weights[i];
        cout << "Ingrese la altura de " << names[i] << ": ";
        cin >> heights[i];
        cin.ignore(); // Limpiar el buffer
    }

    // Encontrar el peso con menor edad
    int minAgeIndex = 0;
    for (int i = 1; i < SIZE; i++) {
        if (ages[i] < ages[minAgeIndex]) {
            minAgeIndex = i;
        }
    }

    // Calcular el promedio de peso y altura
    float totalWeight = 0;
    float totalHeight = 0;
    for (int i = 0; i < SIZE; i++) {
        totalWeight += weights[i];
        totalHeight += heights[i];
    }
    float averageWeight = totalWeight / SIZE;
    float averageHeight = totalHeight / SIZE;

    // Mostrar resultados
    cout << "La persona con menor edad es: " << names[minAgeIndex] << " con un peso de " << weights[minAgeIndex] << " kg." << endl;
    cout << "El promedio de peso es: " << averageWeight << " kg." << endl;
    cout << "El promedio de altura es: " << averageHeight << " m." << endl;

    return 0;
}