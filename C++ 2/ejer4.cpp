//funcion para calcular votos de 3 canditados y mostrar el ganador mas el porcentaje de votos
#include <iostream>
using namespace std;

const int CANDIDATES = 3;

// Función para calcular votos y mostrar ganador
void calcularGanador() {
    int votes[CANDIDATES] = {0}; 
    string candidateNames[CANDIDATES] = {"Candidato A", "Candidato B", "Candidato C"};

    // Ingresar votos para cada candidato
    for (int i = 0; i < CANDIDATES; i++) {
        cout << "Ingrese el numero de votos para " << candidateNames[i] << ": ";
        cin >> votes[i];
    }

    // Calcular el total de votos
    int totalVotes = 0;
    for (int i = 0; i < CANDIDATES; i++) {
        totalVotes += votes[i];
    }

    // Encontrar el ganador
    int winnerIndex = 0;
    for (int i = 1; i < CANDIDATES; i++) {
        if (votes[i] > votes[winnerIndex]) {
            winnerIndex = i;
        }
    }

    // Calcular el porcentaje de votos del ganador
    double winnerPercentage = (static_cast<double>(votes[winnerIndex]) / totalVotes) * 100;

    // Mostrar el ganador y su porcentaje de votos
    cout << "El ganador es: " << candidateNames[winnerIndex] 
         << " con " << winnerPercentage << "% de los votos." << endl;
}

int main() {
    calcularGanador(); // Llamada a la función
    return 0;
}
