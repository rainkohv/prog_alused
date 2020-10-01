fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()

aasta = input("Sisestage aasta: ")

if aasta == "2011":
    print(vastuvõetud[0])
elif aasta == "2012":
    print(vastuvõetud[1])
elif aasta == "2013":
    print(vastuvõetud[2])
elif aasta == "2014":
    print(vastuvõetud[3])
elif aasta == "2015":
    print(vastuvõetud[4])
elif aasta == "2016":
    print(vastuvõetud[5])
elif aasta == "2017":
    print(vastuvõetud[6])
elif aasta == "2018":
    print(vastuvõetud[7])
else:
    aasta == "2019"
    print(vastuvõetud[8])