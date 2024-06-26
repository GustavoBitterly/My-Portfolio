# This is my first Python project. Enjoy, and any feedback is welcome!

import random
import sys

# Welcome to RPG Project, where you are a warrior with the mission
# of delivering a letter to the king as quickly as possible.
# This letter will serve to request reinforcements for your village,
# which is under attack by a horde of demons. But be cautious,
# as you will encounter demons along your journey who will hinder your path. Good luck! 🗡️📜🔥


player_hp = 100
player_choice = 0
random_dodge = 0


player_name = input("\n Enter your name, brave warrior!! \n R:")

if player_hp > 0:
    print(f"\n Welcome {player_name} your adventure begins here")
    print("\n Your village is under attack! 🏰🔥")
    print(
        "\n Quickly, run outside of the village to deliver the letter to the king. 🏃‍♂️📜👑"
    )

    player_choice = int(input("\n 1- Run Outside \n 2- Stay \n R: "))
    if player_choice == 1:
        print(
            "\n Very well, you ran outside of your village with all your might, but the journey is not yet over. 🏃‍♂️💨🌄"
        )
    else:
        print(
            "\n You stayed, and the letter was not delivered. The demons destroyed your village. Game over. 🔥📜😢"
        )
        sys.exit()

    print(
        "\n While you were running toward the castle, you see a demon that will cross your path. 🏰🏃‍♂️👹"
    )

    player_choice = int(input("\n 1- Dodge (50% chance) 🏃‍♂️ \n R: "))
    random_dodge = random.randint(1, 100)

    if player_choice == 1 and random_dodge >= 50:
        print("\n You successfully dodged it; you can continue on your way. 🏃‍♂️👍")
    else:
        print("\n You couldn’t dodge it; get ready for the attack. 🏃‍♂️🔥")
        print("\n Prepare to Die 🔥👹🔥")
        print(f"\n {player_hp} HP {player_name}")
        print("\n The Demon stabs you 👹 -50 HP")
        player_hp -= 80  # Corrected line: decrement player_hp by 80
        print(f"\n {player_hp} HP {player_name}")
        print(
            "\n The Demon doesn't want to waste time with you and left for the village 👹"
        )
        print("\n You are safe now")

    print(
        "\n After escaping from the demon, you continue your path, running toward the castle, but it’s getting dark. 🌙🏰"
    )
    print(
        "\n Already at night, you hear the roar of a demon, so you quickly think about hiding so it doesn’t see you. 👹🌙"
    )

    player_choice = int(input("\n 1- Hide 🏃‍♂️🌙 \n R: "))
    print(
        "\n Scared, while you wait for the demon to leave, you decide to count to 10 to make sure it doesn’t notice you. 👻🕰️"
    )
    for i in range(1, 11):
        print("\n")
        print(i)

    print("\n The devil left without you noticing, and now you are safe")
    print(
        "\n You keep running without stopping until you reach the castle, you enter the king’s chamber and deliver the letter, which, upon finishing reading, immediately mobilizes his troops toward your village"
    )

    if player_hp == 100:
        print(
            "\n After the king’s troops eliminated the demons and saved your village, the king congratulates you and you join his squadron of soldiers"
        )
        print("\n 🎉🎉🎉THANKS FOR PLAYING🎉🎉🎉")
        sys.exit()
    else:
        print(
            "\n The king’s troops successfully eliminated the demons, saving your village. However, due to the wounds you suffered along the way, you did not survive"
        )
        print("\n 🔥🔥🔥THANKS FOR PLAYING🔥🔥🔥")
        sys.exit()

else:
    sys.exit()
