#nime küsimine
name = input("Sisestage leedu perekonnanimi: ")
#kui nime lõpus -ne, prindi "abielus"
if name[-2:] == "ne":
    print("Abielus")
#kui nime lõpus -ne, prindi "vallaline"
elif name[-2:] == "te":
    print("Vallaline")
#kui nime lõpus -e, prindi "määramata"
elif name[-1:] == "e":
    print("Määramata")
#kui ei vasta ühelegi tingimusele, prindi "pole ilmselt leedu perekonnanimi"
else:
    print("Pole ilmselt leedu perekonnanimi")