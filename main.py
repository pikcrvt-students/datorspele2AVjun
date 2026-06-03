from figuras import figuras, noteikumi


def virsraksts(text):
    print("\n" + text)
    print("-" * len(text))


def paradit_galdu(galds):
    for rinda in galds:
        for lauks in rinda:
            print(lauks, end=" ")
        print()


galds = [
    ["T", "Z", "L", "D", "K", "L", "Z", "T"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["t", "z", "l", "d", "k", "l", "z", "t"]
]

virsraksts("Saha apmacibas programma")

virsraksts("Saha galds")
paradit_galdu(galds)

virsraksts("Saha figuras")
figuras()

virsraksts("Saha noteikumi")
noteikumi()