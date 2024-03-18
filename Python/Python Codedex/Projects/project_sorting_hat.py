gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
casaGanadora = 0

questionOne = int(input("Q1) Do you like Dawn or Dusk? \n 1) Dawn \n 2) Dusk \n R: "))

if questionOne == 1:
    gryffindor += 1
    ravenclaw += 1
elif questionOne == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

questionTwo = int(
    input(
        "Q2) When I’m dead, I want people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n R: "
    )
)

if questionTwo == 1:
    hufflepuff += 2
elif questionTwo == 2:
    slytherin += 2
elif questionTwo == 3:
    ravenclaw += 2
elif questionTwo == 4:
    gryffindor += 2
else:
    print("Wrong input.")

questionThree = int(
    input(
        "Q3) Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum \n R: "
    )
)

if questionThree == 1:
    slytherin += 4
elif questionThree == 2:
    hufflepuff += 4
elif questionThree == 3:
    ravenclaw += 4
elif questionThree == 4:
    gryffindor += 4
else:
    print("Wrong input.")

casaGanadora = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if casaGanadora == gryffindor:
    print("Tu casa es Gryffindor!!")
elif casaGanadora == ravenclaw:
    print("Tu casa es Ravenclaw!!")
elif casaGanadora == hufflepuff:
    print("Tu casa es Hufflepuff!!")
else:
    print("Tu casa es Slytherin!!")
