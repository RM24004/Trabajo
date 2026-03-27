//vocales en una palabra insertada por el usuario utilizando punteros
#include <iostream>
#include <cctype>
#include <string>
using namespace std;

void contarVocales(const char *palabra, int &contadorA, int &contadorE, int &contadorI, int &contadorO, int &contadorU) {
    while (*palabra != '\0') { // mientras no se alcance el final de la cadena
        switch (tolower(*palabra)) { // convertir el caracter a minúscula
            case 'a': contadorA++; break;
            case 'e': contadorE++; break;
            case 'i': contadorI++; break;
            case 'o': contadorO++; break;
            case 'u': contadorU++; break;
        }
        palabra++; // mover el puntero al siguiente caracter
    }
}

int main() {
    string palabra;
    cout << "Ingrese una palabra: ";
    cin >> palabra;

    // Inicializar contadores
    int contadorA = 0, contadorE = 0, contadorI = 0, contadorO = 0, contadorU = 0;

    // Llamar a la función con punteros
    contarVocales(palabra.c_str(), contadorA, contadorE, contadorI, contadorO, contadorU);

    // Mostrar resultados
    cout << "La palabra es: " << palabra << endl;
    cout << "Cantidad de vocales:" << endl;
    cout << "A: " << contadorA << endl;
    cout << "E: " << contadorE << endl;
    cout << "I: " << contadorI << endl;
    cout << "O: " << contadorO << endl;
    cout << "U: " << contadorU << endl;

    return 0;
}
