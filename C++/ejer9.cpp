//leer frase, separar palabras y mostrar cada palabra en una línea diferente contando la cantidad de caracteres de cada palabra
#include <iostream>
#include <sstream>
using namespace std;
int main() {
    string frase;
    cout << "Ingrese una frase: ";
    getline(cin, frase); // Lee la frase completa, incluyendo espacios

    stringstream ss(frase); // Crea un stringstream para separar las palabras
    string palabra;

    cout << "\nPalabras y su cantidad de caracteres:" << endl;
    while (ss >> palabra) { // Extrae cada palabra del stringstream
        cout << palabra << " - " << palabra.length() << " caracteres" << endl; // Muestra la palabra y su longitud
    }

    return 0;
}