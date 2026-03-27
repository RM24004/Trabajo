// pedir una cadena de caracteres al usuario, y contar cuandas veces aparece cada vocal utilizando punteros
#include <iostream>
#include <cctype>
#include <string>
using namespace std;

void contarVocales(const char *frase, int &contadorA, int &contadorE, int &contadorI, int &contadorO, int &contadorU) {
    while (*frase != '\0') { // mientras no se alcance el final de la cadena
        switch (tolower(*frase)) { // convertir el caracter a minúscula
            case 'a': contadorA++; break;
            case 'e': contadorE++; break;
            case 'i': contadorI++; break;
            case 'o': contadorO++; break;
            case 'u': contadorU++; break;
        }
        frase++; // mover el puntero al siguiente caracter
    }
}

int main() {
    string frase;
    cout << "Ingrese una frase: ";
    getline(cin, frase); // permite capturar frases completas con espacios

    // Inicializar contadores
    int contadorA = 0, contadorE = 0, contadorI = 0, contadorO = 0, contadorU = 0;

    // Llamar a la función con punteros
    contarVocales(frase.c_str(), contadorA, contadorE, contadorI, contadorO, contadorU);

    // Mostrar resultados
    cout << "La frase es: \"" << frase << "\"" << endl;
    cout << "Cantidad de vocales:" << endl;
    cout << "A: " << contadorA << endl;
    cout << "E: " << contadorE << endl;
    cout << "I: " << contadorI << endl;
    cout << "O: " << contadorO << endl;
    cout << "U: " << contadorU << endl;

    // Total de vocales
    int total = contadorA + contadorE + contadorI + contadorO + contadorU;
    cout << "Total de vocales: " << total << endl;

    return 0;
}
