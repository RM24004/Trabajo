##convertir de romano a entero
class RomanConverter:
    def __init__(self):
        self.roman_map = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

    def roman_to_int(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # Si hay un símbolo siguiente y su valor es mayor, es una resta (ej. IV = 4)
            if i + 1 < len(s) and self.roman_map[s[i]] < self.roman_map[s[i + 1]]:
                total += self.roman_map[s[i + 1]] - self.roman_map[s[i]]
                i += 2
            else:
                total += self.roman_map[s[i]]
                i += 1
        return total


def main():
    try:
        roman_num = input("Ingrese un número romano (ej. MCMXCIV): ").upper()
        converter = RomanConverter()
        result = converter.roman_to_int(roman_num)
        print(f"El número romano {roman_num} equivale a {result} en entero.")
    except KeyError:
        print("Error: número romano inválido.")


if __name__ == "__main__":
    main()
