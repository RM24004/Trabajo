//definir la estructura para ciclista (hora, minutos, segundos), pedirle al usuario los datos de 3 etapas y calcular el tiempo total de cada etapa, y mostrar el tiempo total del ciclista
#include <iostream>
using namespace std;

struct Ciclista {
    int hora;
    int minutos;
    int segundos;
};

// Función que recibe un puntero a Ciclista y devuelve el tiempo en segundos
int calcularSegundos(Ciclista *etapa) {
    return (etapa->hora * 3600) + (etapa->minutos * 60) + etapa->segundos;
}

int main() {
    const int SIZE = 3;
    Ciclista etapas[SIZE];

    // Pedir datos de las etapas usando punteros
    for (int i = 0; i < SIZE; i++) {
        Ciclista *ptr = &etapas[i]; // puntero a la etapa actual
        cout << "Ingrese la hora de la etapa " << i + 1 << ": ";
        cin >> ptr->hora;
        cout << "Ingrese los minutos de la etapa " << i + 1 << ": ";
        cin >> ptr->minutos;
        cout << "Ingrese los segundos de la etapa " << i + 1 << ": ";
        cin >> ptr->segundos;
    }

    // Calcular el tiempo total del ciclista usando punteros
    int totalSegundos = 0;
    for (int i = 0; i < SIZE; i++) {
        totalSegundos += calcularSegundos(&etapas[i]);
    }

    // Convertir el tiempo total a horas, minutos y segundos
    int horasTotales = totalSegundos / 3600;
    int minutosTotales = (totalSegundos % 3600) / 60;
    int segundosTotales = totalSegundos % 60;

    // Mostrar el tiempo total del ciclista
    cout << "\nEl tiempo total del ciclista es: "
         << horasTotales << " horas, "
         << minutosTotales << " minutos, "
         << segundosTotales << " segundos." << endl;

    return 0;
}

