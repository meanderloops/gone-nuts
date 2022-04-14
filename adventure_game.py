import time
import random


def print_pause(string):
    # sets pacing for most print statements in game
    print(string)
    time.sleep(2)
    print()


def title_card():
    print()
    print_pause((" 8888888888888888888888\n"
                 " 8888888        8888888\n"
                 " 8888888  GONE  8888888\n"
                 " 8888888  NUTS  8888888\n"
                 " 8888888        8888888\n"
                 " 8888888888888888888888"))

    # leads to...
    part_one()


def part_one():
    # introduction
    print_pause(("You find yourself standing in the middle "
                 "of a grocery store aisle."))
    print_pause("50 different brands of nuts surround you.")
    print_pause("Your favorite kind is sold out.")
    print_pause("But you gotta have them nuts.")

    # leads to...
    choice1()


def choice1():
    # interaction for part_one
    print_pause("What would you like to do?")
    choice = input(("1)  Go with a different kind.\n"
                    "2)  Wait for a miracle.\n"))

    if choice == '1':
        # leads to a random ending
        print()
        print_pause("You decide to just go with one of the generic options.")
        random_ending()
    elif choice == '2':
        part_two()
    else:
        invalid_input()
        choice1()


def part_two():
    # the Peanut appears
    print()
    print_pause("After a few moments, you feel a shift in your surroundings.")
    print_pause("The miracle is on its way.")
    print_pause(("A yellow peanut, the same size as you, appears "
                 "around the corner."))
    print_pause("It swaggers towards you with its cane, monocle, and top hat.")
    print_pause("On arrival, it speaks...")
    print_pause('"Why hello there, young one."')
    print_pause('"I know of what you seek and I can take you to it."')
    print_pause("\"Please, will you follow me? It's only a short trek.\"")

    # leads to...
    choice2()


def choice2():
    # interaction for part_two
    print_pause("Do you follow the Peanut?")
    choice = input(("1)  Sure. I'm digging its style.\n"
                    "2)  Nah. I don't trust food that speaks.\n"))

    if choice == '1':
        part_three()
    elif choice == '2':
        # leads to a random ending
        print()
        print_pause(("You ignore the interaction and grab a random "
                     "jar of nuts."))
        print_pause("Leaving the talking Peanut behind, you head to checkout.")
        random_ending()
    else:
        invalid_input()
        choice2()


def part_three():
    # journey to *THE CEREAL AISLE*
    print()
    print_pause("You follow the Peanut out of the aisle and into another.")
    print_pause("The people you pass along the way take no interest.")
    print_pause("To them, there's no oddity here. Just groceries.")
    print_pause('The Peanut stops ahead of you, in the cereal aisle.')
    print_pause('You see them greet another figure before addressing you.')
    print_pause('"We have arrived," the Peanut says.')

    # leads to...
    choice3()


def choice3():
    # interaction for part_three
    # this choice (mascot) will determine what happens in part_five
    print_pause('"What do you see?"')
    choice = input(("1)  A full-sized tiger wearing a red kerchief.\n"
                    "2)  A full-sized leprechaun wearing... "
                    "leprechaun attire.\n"))

    if choice == '1':
        mascot = 'tiger'
        part_four(mascot)
    elif choice == '2':
        mascot = 'leprechaun'
        part_four(mascot)
    else:
        invalid_input()
        choice3()


def part_four(mascot):
    # the Void is noticed
    print()
    print_pause('"Look closer," the Peanut replies.')
    print_pause('"Focus."')
    print_pause("You look closer at the gallery of cereal boxes.")
    print_pause(("In the wall of colorful cardboard faces, "
                 "there's one that's missing."))
    print_pause("Another sold out item. Another hole.")
    print_pause("You peek into its depths.")
    print_pause('The darkness seems to go on forever.')

    # leads to...
    choice4(mascot)


def choice4(mascot):
    # interaction for part_four
    print_pause("Do you reach into the void?")
    choice = input(("1)  Well yeah, I've already gone this far. "
                    "Might as well.\n"
                    "2)  No. I'm done. Get me outta here.\n"))

    if choice == '1':
        part_five(mascot)
    elif choice == '2':
        # leads to a random ending
        print()
        print_pause("You head back to the nuts section and grab whatever.")
        random_ending()
    else:
        invalid_input()
        choice4(mascot)


def part_five(mascot):
    # the reach into the unknown
    print()
    print_pause("Your whole arm disappears into the unknown.")
    print_pause("You feel nothing at first.")
    print_pause("You look back at the Peanut.")
    print_pause("Fluorescent lights above reflect on its monocle.")
    print_pause("The Peanut then gives you an affirming nod.")

    # the mascot variable from choice3 gets used here
    if mascot == 'tiger':
        print_pause('The Tiger also provides a grrrrrreat nod.')
    else:
        print_pause('Additionally, the Leprechaun gives you a magical nod.')

    # leads to...
    choice5()


def choice5():
    # interaction for part_five
    # this "choice" intentionally lacks conditional statements
    print_pause("How do you feel?")
    input(("1)  scared\n"
           "2)  happy\n"
           "3)  potato\n"
           "4)  hungry\n"))

    # leads to...
    part_six()


def part_six():
    # freaky hole doing freaky things
    print()
    print_pause("Then, the lights begin to flicker.")
    print_pause("A coldness creeps in.")
    print_pause("Goosebumps form on your skin.")
    print_pause("Your heart rate rises.")
    print_pause("In a panic, you pull your arm out.")
    print_pause("The Peanut makes its way over to you.")
    print_pause("Their presence seems to calm you.")
    print_pause("It looks down at your hands and begins to speak.")
    print_pause('"It appears you have good taste in snacks."')
    print_pause(("With your heart now stabilized, you look down "
                 "at your hands..."))

    # leads to...
    choice6()


def choice6():
    # interaction for part_six
    # determines the ending
    print_pause("What are you holding?")
    choice = input(("1)  Cashews!\n"
                    "2)  Peanuts!\n"
                    "3)  Non-Fat Low-Sodium Clam Chowder?!\n"))

    if choice == '1':
        cashew_end()
    elif choice == '2':
        peanut_end()
    elif choice == '3':
        chowder_end()
    else:
        invalid_input()
        choice6()


def cashew_end():
    # ending for cashew selection
    print()
    print_pause("There they are. Your precious cashews.")
    print_pause("For just a moment, balance in the universe is restored.")
    print_pause("You look around to thank the Peanut.")
    print_pause("But you are alone.")
    print_pause("You pay for the cashews and head out of the grocery store.")
    print_pause(("You'll remember what the Peanut did for you during "
                 "desperate times."))
    print_pause("One day, you'll tell your children about the Peanut.")
    print_pause("They will envy you.")
    print_pause("During the ride home, you enjoy your cashews.")
    print_pause("THE END")

    # asks player if they want to replay
    play_again()


def peanut_end():
    # ending for peanut selection
    print()
    print_pause("There they are. Your lovely peanuts.")
    print_pause("For just a moment, things feel right.")
    print_pause("You look around to give thanks to the Peanut.")
    print_pause("But they're gone.")
    print_pause(("As you leave the grocery store, you ponder the nature "
                 "of the Peanut."))
    print_pause("Where did it come from?")
    print_pause("What kind of music does it like?")
    print_pause("Wait, does it too... eat peanuts?")
    print_pause("You have many questions.")
    print_pause("None will be answered.")
    print_pause("But hey, at least you now have some tasty peanuts.")
    print_pause("THE END")

    # asks player if they want to replay
    play_again()


def chowder_end():
    # ending for chowder selection
    print()
    print_pause("Well, this isn't what you were looking for.")
    print_pause("Like, not even close.")
    print_pause("You look around to question the Peanut.")
    print_pause("But they've disappeared.")
    print_pause("You head to checkout and buy the chowder anyway.")
    print_pause("You don't know why.")
    print_pause("However, on your ride home you remember something.")
    print_pause("Your parents.")
    print_pause("They love clam chowder!")
    print_pause("So, you make a detour and head to your parents' place.")
    print_pause("When you arrive, you hand them the chowder.")
    print_pause("Both of them nearly come to tears.")
    print_pause("After many thanks, they too have something to give.")
    print_pause("Nuts!")
    print_pause("It's your favorite kind.")
    print_pause("THE END")

    # asks player if they want to replay
    play_again()


def random_ending():
    # endings for when the player rejects the Peanut's guidance
    endings = [(("The nuts you selected were pretty good and became "
                 "a new favorite.")),
               ("Whatever you selected was SO BAD you never ate nuts again."),
               (("The nuts were fine, but you don't know if you'll "
                 "ever recover from this."))]
    print_pause(random.choice(endings))
    print_pause("THE END?")

    # asks player if they want to replay
    play_again()


def play_again():
    # exits game or resets to beginning of game
    print_pause("Would you like to play again?")
    choice = input(("1)  Yes.\n"
                    "2)  No.\n"))

    if choice == '1':
        print()
        play_game()
    elif choice == '2':
        print()
        print_pause("Goodbye! Thanks for playing!")
        exit()
    else:
        invalid_input()
        play_again()


def invalid_input():
    # message for player if they give invalid answer
    print()
    print_pause(("Please pick an appropriate answer. "
                 "This is very important stuff."))


def play_game():
    title_card()


play_game()
