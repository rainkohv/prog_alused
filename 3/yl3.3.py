#muutujate deklareerimine
n_of_dice = int(input("Sisesta täringute arv: "))
i = 0
#mooduli import täringuviske jaoks
from random import randint
#tsükkel kus muutuja i itereerib end seni kuni on võrdne kasutaja sisestatuga
while i < n_of_dice:
    print(str(randint(1, 6)))
    i += 1