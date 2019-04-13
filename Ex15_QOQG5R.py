from itertools import permutations

try:
    szam = []

    for i in range(5):
        szam.append(int(input("{}. szam = ".format(i+1))))

    eredmeny = list(permutations(szam))

    for szam in eredmeny:
        epit = ""
        for i in szam:
            if epit == "" and i == 0:
                continue
            else:
                epit += str(i)

        print(epit)

except ValueError:
    print("A beolvasott ertek egesz szam kell legyen")