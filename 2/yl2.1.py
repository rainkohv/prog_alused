temp = (input("Sisestage õhutemperatuur: "))
temp_oht = 4
#kui temp_oht on suurem või võrdne kui temp, siis prindi ohuteade.
if float(temp) >= float(temp_oht):
    print("Ei ole jäätumise ohtu.")

else: print("On jäätumise oht")