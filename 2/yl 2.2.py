name = input("Sisestage leedu perekonnanimi: ")

if name[-2:] == "ne":
    print("Abielus")

if name[-2:] == "te":
    print("Vallaline")

if name[-1:] == "e" and name[-2:] != "te" and name[-2:] != "ne":
    print("Määramata")

else :
    print("Pole ilmselt leedu perekonnanimi")