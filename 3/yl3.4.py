#pöialpoisside arv
n_of_users = int(input("Mitu pöialpoissi soovib õunu? "))
i = 0
from random import randint
sum_of_apples = 0
#õunte loosimine pöialpoistele
while i < n_of_users:
    i += 1
    n_of_apples = (randint(1, 2))
    print(str(n_of_apples))
# loositud õunte liitmine
    sum_of_apples += n_of_apples
#lumivalgekese õunte arvutamine
print ("Lumivalgekesele jäi " + str(14 - (int(sum_of_apples))) + " õuna.")