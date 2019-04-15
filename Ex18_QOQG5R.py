from itertools import product

def keres(szamok, muveletek):
    for muvelet in muveletek:
        szoveg = str(szamok[0])
        for i in range(1, len(szamok)):
            if muvelet[i - 1] == "+":
                szoveg += " + "
                szoveg += str(szamok[i])
            elif muvelet[i - 1] == "-":
                szoveg += " - "
                szoveg += str(szamok[i])
            elif muvelet[i - 1] == "":
                szoveg += str(szamok[i])

        p = "+"
        sz = szoveg.split(" ")
        i = 0
        sum = 0
        while i < len(sz):
            if sz[i] == "+":
                p = "+"
                i += 1
            elif sz[i] == "-":
                p = "-"
                i += 1
            else:
                tmp = 0
                while i < len(sz) and sz[i] != "-" and sz[i] != "+":
                    tmp *= 10
                    tmp += int(sz[i])
                    i += 1

                if p == "+":
                    sum += tmp
                elif p == "-":
                    sum -= tmp

        if sum == 100:
            print(szoveg, "= ", sum)


try:
    szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    muv = ["+", "-", ""]

    muveletek = []

    for m in product(muv, repeat=8):
        muveletek.append(m)

    keres(szamok, muveletek)

except NameError:
    print("Hibas fugvenyhivas")
