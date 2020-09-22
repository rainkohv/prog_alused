mail_size = float(input("Sisestage kirja suurus megabaitides: "))
subject = input("Sisestage kirja teema pealkiri, pealkirja puudumisel ärge sisestage midagi: ")
attachment = input("Kas kirjale on lisatud manus?: ")

if subject != "" or (mail_size > 1.0 and attachment == "jah"):
    print("Kiri ei ole spämm")
else:
    print("Kiri on spämm")
