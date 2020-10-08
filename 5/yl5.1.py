#loeme failist andmed ja lisame ühe kaupa nimekirja
fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in fail:
     vastuvoetud.append(int(rida))
fail.close()
#küsime aastaarvu
aasta = int(input("Sisestage aasta: "))
#aastate nimekiri
aastad = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

if aasta in aastad:
    #vaja teada mis indeksiga antud aasta nimekirjas on
    i = aastad.index(aasta)
    #prindi sama indeksiga väärtus nimekirjast
    print("Aastas " + str(aasta) + " võeti vastu " + str(vastuvoetud[i]))
