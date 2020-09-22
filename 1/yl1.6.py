#ülesande 1.6 lahendus.

max_kohad_bussis = int (input("Sisestage kohtade arv bussis: "))
inimeste_arv = int(input("Sisestage inimeste arv: "))
busside_arv = int(inimeste_arv / max_kohad_bussis)
maha_inimesed =  inimeste_arv % max_kohad_bussis

print("Inimeste transpordiks on vajalik tellida " + str(busside_arv) + " buss(i).")
print("Bussi(desse) ei mahu " + str(maha_inimesed) + " inimest.")
