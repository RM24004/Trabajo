## convertir un numero entero ingresado por el usuario a numnero romano
class RomanConverter:
    def __init__(self):
        self.val = [1000, 900, 500, 400,
                    100, 90, 50, 40,
                    10, 9, 5, 4,
                    1]
        self.syms = ["M", "CM", "D", "CD",
                     "C", "XC", "L", "XL",
                     "X", "IX", "V", "IV",
                     "I"]

    def int_to_roman(self, num: int) -> str:
        if num <= 0 or num > 3999:
            raise ValueError("El número debe estar entre 1 y 3999")

        roman_num = ""
        i = 0
        while num > 0:
            count = num // self.val[i]       # cuántas veces cabe el valor
            roman_num += self.syms[i] * count
            num %= self.val[i]               # resto
            i += 1
        return roman_num


def main():
    try:
        num = int(input("Ingrese un número entero (1-3999): "))
        converter = RomanConverter()
        print(f"El número {num} en números romanos es: {converter.int_to_roman(num)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
