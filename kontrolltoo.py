#importime random mooduli
import random
#defineerime funktsiooni
def kone_maksumus(kone_kestus_sek, kone_minuti_hind):
    # Kõne hind minimaalselt 1 minuti kohta
    if kone_kestus_sek < 60:
        return kone_minuti_hind

    # Kõne hind maksimaalselt 10 minuti kohta
    if kone_kestus_sek > 600:
        return kone_minuti_hind * 10
    #Teisendamine sekunditeks
    kone_sekundi_hind = kone_minuti_hind / 60
    return round((kone_sekundi_hind * kone_kestus_sek), 2)

#juhusliku arvu seed
random.seed()
#kasutajalt info sisestamine
hind = float(input("Sisestage kõneminuti hind: "))
konede_koguarv = int(input("Sisestage kõnede arv: "))

#anname kõnedele juhusliku kestvuse 1 sekundi ja 1000 sekundi vahel
konede_kestvus = []
for x in range(konede_koguarv):
    konede_kestvus.append(random.randrange(1, 1000))

#arvutame iga kõne hinna ja kõikide kõnede hinnad for tsükli abil
kogumaksumus = 0
for y in range(len(konede_kestvus)):
    hetke_hind = kone_maksumus(konede_kestvus[y], hind)
    kogumaksumus += hetke_hind
    print("Kõne maksumus: " + str(hetke_hind) + "€")

print("Kogumaksumus: " + str(kogumaksumus))
