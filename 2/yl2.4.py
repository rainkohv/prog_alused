from random import randint
user_seat = ""
user_choice = input("Kas soovite istekohta ise valida (\"ise\") või loosida (\"loos\")?")
if user_choice == "ise":
    user_seat_choice = input("Kas soovite istuda akna ääres (\"aken\") või mitte (\"muu\")? ")

    if user_seat_choice == "aken":
        print ("Valisite ise. Aknakoht.")
    else:
        user_seat == "muu"
        print("Valisite ise. Vahekäigukoht")

if user_choice == "loos":
    seat_chance = randint(1, 3)
    if seat_chance == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print ("Istekoht loositi. Vahekäigukoht")


