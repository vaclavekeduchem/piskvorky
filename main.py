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
    vyhra = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3], [1, 5, 9], [3, 5, 7]]
    hrac = ""
    hraci = ["X", "O"]

    print("Piškvorky")
    while True:

        # Výběr strany
        while hrac not in hraci:
            hrac = input("Vyber si stranu (X/O): ")

        # Ovládání celé hry
        while True:

            numpad_value = input(f"Hraješ {hrac}, vyber si pole (1-9): ")
            if numpad_value.isnumeric():
                numpad_value = int(numpad_value)

                if hraci_pole[cislo_na_index(numpad_value)] not in hraci:
                    hraci_pole[cislo_na_index(numpad_value)] = hrac
                    break

        vypis_hraci_pole(hraci_pole)

        # Validace výhra
        for v in vyhra:
            if hraci_pole[v[0] - 1] == hrac and hraci_pole[v[1] - 1] == hrac and hraci_pole[v[2] - 1] == hrac:
                print(f"{hrac} vyhrál!")
                exit()

        # Přehození stran
        if hrac == hraci[0]:
            hrac = hraci[1]
        else:
            hrac = hraci[0]


if __name__ == "__main__":
    main()
