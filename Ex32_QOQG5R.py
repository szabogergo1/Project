import numpy as np


def epit(pir):
    i = 0
    szam = 1

    while i <= N and szam <= N:
        pir[i][N] = szam
        jobb = N - 1
        bal = N + 1
        jobbertek = szam - 1
        balertek = szam - 1

        while jobbertek > 0:
            pir[i][jobb] = jobbertek
            pir[i][bal] = balertek
            jobbertek -= 1
            balertek -= 1
            jobb -= 1
            bal += 1

        szam += 1
        i += 1


def filebeir(pir, fo, n):
    for i in range(n):
        for j in range(1, 2*n):
            if pir[i][j] == 0:
                print(" ", end=" ", file=fo)
            else:
                print(pir[i][j] % 10, end=" ", file=fo)

        print(file=fo)


try:
    f = open("output.txt", "w")
    N = int(input("Adja meg a szamot: "))

    piramis = np.zeros((N, 2*N), dtype=int)

    epit(piramis)

    filebeir(piramis, f, N)

    f.close()

except (ValueError, NameError, FileNotFoundError):
    print("Az adott ertek 0-nal nagyobb termeszetes szam (int) kell legyen.")
