#Ülesande 1.4 lahendus

nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int (input("Sisestage lubatud kiirus: "))
tegelik_kiirus = int (input("Sisestage teie tegelik kiirus: "))

trahvisumma = (tegelik_kiirus - lubatud_kiirus)*3

print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahvisumma) + " eurot.")