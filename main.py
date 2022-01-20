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
def cislo_na_index(hraci_pole: list, numpad_value: int, hrac: str):
    match numpad_value:
        case 1:
            hraci_pole[6] = hrac
        case 2:
            hraci_pole[7] = hrac
        case 3:
            hraci_pole[8] = hrac
        case 7:
            hraci_pole[0] = hrac
        case 8:
            hraci_pole[1] = hrac
        case 9:
            hraci_pole[2] = hrac
        case _:
            hraci_pole[numpad_value - 1] = hrac


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
        numpad_value = int(input("Vyber si pole (1-9): "))
        cislo_na_index(hraci_pole, numpad_value, hrac)

        vypis_hraci_pole(hraci_pole)

        # Přehození stran
        if hrac == hraci[0]:
            hrac = hraci[1]
        else:
            hrac = hraci[0]


if __name__ == "__main__":
    main()
