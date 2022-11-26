def BubbleSort(zoz: list) -> list:
    for i in range(len(zoz)-1):
        for j in range(len(zoz)-i-1):
            if zoz[j] > zoz[j+1]:
                zoz[j], zoz[j+1] = zoz[j+1], zoz[j]
    return zoz


zoznam = [5, 8, 13, 2, 58, 42, 101]
print(BubbleSort(zoznam))
