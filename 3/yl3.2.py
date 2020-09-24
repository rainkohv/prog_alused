#While tsükkel vältimaks programmi "lühisesse" minemast kui sisendiks on midagi muud kui positiivne number
while True:
  number_of_laps = 0
  lap_input = input("Sisesta ringide arv: ")
  if(lap_input.isdigit()):
    number_of_laps = int(lap_input)
    if(number_of_laps <= 0):
      print("Ringide arv peab olema positiivne arv!")
      continue
    else:
        total_rewards = 0
        lap_counter = 0
        while lap_counter <= number_of_laps:
            total_rewards += lap_counter
            lap_counter += 2
        print("Porgandite koguarv on " + str(total_rewards))
    break
  else:
    print("Ringide arv peab olema positiivne arv!")
    continue


