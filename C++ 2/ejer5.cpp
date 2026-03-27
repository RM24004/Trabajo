//ingresaremos un numero de estudaintes y sus notas, luego mostraremos el promedio de cada estudiante, el mejor promedio y el peor promedio
// debemos de solicitar los datos nombre, apellido, semestre, materia y nota1, nota2, nota3
#include <iostream>
#include <string>
using namespace std;
int main() {
    int numStudents;
    cout << "Ingrese el numero de estudiantes: ";
    cin >> numStudents;
    cin.ignore(); // Limpiar el buffer

    string names[numStudents];
    string lastNames[numStudents];
    int semesters[numStudents];
    string subjects[numStudents];
    float grades[3][numStudents]; // 3 notas por estudiante

    // Ingresar datos de los estudiantes
    for (int i = 0; i < numStudents; i++) {
        cout << "Ingrese el nombre del estudiante " << i + 1 << ": ";
        getline(cin, names[i]);
        cout << "Ingrese el apellido del estudiante " << i + 1 << ": ";
        getline(cin, lastNames[i]);
        cout << "Ingrese el semestre del estudiante " << i + 1 << ": ";
        cin >> semesters[i];
        cin.ignore(); // Limpiar el buffer
        cout << "Ingrese la materia del estudiante " << i + 1 << ": ";
        getline(cin, subjects[i]);
        
        for (int j = 0; j < 3; j++) {
            cout << "Ingrese la nota " << j + 1 << " del estudiante " << i + 1 << ": ";
            cin >> grades[j][i];
        }
        cin.ignore(); // Limpiar el buffer
    }

    // Calcular promedios y encontrar mejor y peor promedio
    float averages[numStudents];
    float bestAverage = -1; // Inicializar con un valor muy bajo para encontrar el mejor promedio
    float worstAverage = 101; // Inicializar con un valor muy alto para encontrar el peor promedio
    int bestStudentIndex = -1; // Índice del estudiante con el mejor promedio
    int worstStudentIndex = -1; // Índice del estudiante con el peor promedio

    for (int i = 0; i < numStudents; i++) {
        averages[i] = (grades[0][i] + grades[1][i] + grades[2][i]) / 3;
        if (averages[i] > bestAverage) {
            bestAverage = averages[i];
            bestStudentIndex = i;
        }
        if (averages[i] < worstAverage) {
            worstAverage = averages[i];
            worstStudentIndex = i;
        }
    }

    // Mostrar resultados
    cout << endl;
    cout << "Promedios de los estudiantes:" << endl;
    for (int i = 0; i < numStudents; i++) {
        cout << names[i] << " " << lastNames[i] << " - Promedio: " << averages[i] << endl;
    }
    cout << endl;
    cout<< "Resultados:" << endl;
    cout << "El mejor promedio es de: " << names[bestStudentIndex] << " " << lastNames[bestStudentIndex] << " con un promedio de " << bestAverage << endl;
    cout << "El peor promedio es de: " << names[worstStudentIndex] << " " << lastNames[worstStudentIndex] << " con un promedio de " << worstAverage << endl;    
    return 0;
}

