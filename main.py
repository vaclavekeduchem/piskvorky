# Vypíše hrací pole
def vypis_hraci_pole(hraci_pole: list):
    pole = ""
    for i, x in enumerate(hraci_pole):
        if (i + 1) % 3 == 0:
            pole += " " + x + "\n"
        else:
            pole += " " + x
    print(pole)


# Převede hodnoty num. klávesnice na index pole
def cislo_na_index(numpad_value: int):
    match numpad_value:
        case 1:
            return 6
        case 2:
            return 7
        case 3:
            return 8
        case 7:
            return 0
        case 8:
            return 1
        case 9:
            return 2
        case _:
            return numpad_value - 1

def main():
    hraci_pole = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
    hrac = ""
    hraci = ["X", "O"]

    print("Piškvorky")
    while True:

        # Výběr strany
        while hrac not in hraci:
            hrac = input("Vyber si stranu (X/O): ")

        # Ovládání celé hry
        while True:
            numpad_value = int(input("Vyber si pole (1-9): "))
            if hraci_pole[cislo_na_index(numpad_value)] not in hraci:
                hraci_pole[cislo_na_index(numpad_value)] = hrac
                break


        vypis_hraci_pole(hraci_pole)

        # Přehození stran
        if hrac == hraci[0]:
            hrac = hraci[1]
        else:
            hrac = hraci[0]


if __name__ == "__main__":
    main()
