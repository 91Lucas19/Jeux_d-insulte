import time, sys
from random import *
from Personnage import Bernard
from Personnage import Jacquie
from Personnage import Louis
from Personnage import Vlad
from Personnage import Erica
from Personnage import Stella
from Personnage import Enfant
from random import randint
player1 = 1
player2 = 2

def help():
    print("Faudra ecrire l'aide")

    choix = (input("> "))

    while choix != "back":
        print("I didn't quite understand... You have to write 'back'. Try again!")
        choix = (input("> "))

    if choix == "back":
        menu_ecran_titre()


def credits():
    print("""\

   ___ ___ ___ ___ ___ _____ ___ 
  / __| _ \ __|   \_ _|_   _/ __|
 | (__|   / _|| |) | |  | | \__ \_
  \___|_|_\___|___/___| |_| |___/                                

                        """)
    print("CREDITS TJR FAUT TROUVER UN NOM")
    print("---------------------------------")
    print("Created with love by these three")
    print("Axel ASSELOT")
    print("Sasiya")
    print("Lucas Compiano")
    print("Thank you for your attention")
    print("To return to the menu, type 'back'.")
    choix = (input("> "))
    while choix != "back":
        print("Definitely, writing 'back' is harder than I thought... You have to write 'back'. Try again!")
        choix = (input("> "))
    if choix == "back":
        menu_ecran_titre()


def quit():
    print("Thank you for playing")
    exit()


def menu_ecran_titre():
    print('\n'
          '          Welcome to ptn faut trouver un nom \n'
          '              1 - New game               \n'
          '              2 - Help                   \n'
          '              3 - Credits                \n'
          '              4 - Quit                   \n'
          )
    choix = int(input("> "))
    if choix == 1:
        New_game()

    elif choix == 2:
        help()

    elif choix == 3:
        credits()

    elif choix == 4:
        quit()


def intro_titre():
    print("          ____________________________"), time.sleep(0.1)
    print("         !\_________________________/!\ "), time.sleep(0.1)
    print("         !!   FAUT TROUVER UN NOM   !! \ "), time.sleep(0.1)
    print("         !!                MDRR     !!  \ "), time.sleep(0.1)
    print("         !!                         !!  !"), time.sleep(0.1)
    print("         !!       LOADING           !!  !"), time.sleep(0.1)
    print("         !!       .......           !!  !"), time.sleep(0.1)
    print("         !!                         !!  !"), time.sleep(0.1)
    print("         !!                         !!  !"), time.sleep(0.1)
    print("         !!                         !!  /"), time.sleep(0.1)
    print("         !!_________________________!! /"), time.sleep(0.1)
    print("         !/_________________________\!/"), time.sleep(0.1)
    print("            __\_________________/__/!_"), time.sleep(0.1)
    print("           !_______________________!/"), time.sleep(0.1)
    print("         ________________________"), time.sleep(0.1)
    print("        /oooo  oooo  oooo  oooo /!"), time.sleep(0.1)
    print("       /ooooooooooooooooooooooo/ /"), time.sleep(0.1)
    print("      /ooooooooooooooooooooooo/ /"), time.sleep(0.1)
    print("     /C=_____________________/_/"), time.sleep(0.1)
    time.sleep(0)
    menu_ecran_titre()

#Variable personnage:
def stats_B():
    print("BERNARD")
    Synopsis_Bernard = "An 83 year old, he lives alone with no family, he hates people and especially young people. " \
        "What he likes most of all is to have the last word."
    bernard_stats = Bernard(100, 8, Synopsis_Bernard)
    print("Synopsis: ", bernard_stats.Synopsis)
    print("attack: ", bernard_stats.Attack)
    print("Defense: ", bernard_stats.DEF)


def stats_J():
    print("JACQUIE")
    Synopsis_Jacquie = " A 53 year old, he used his children's purse to buy a car. " \
                           "He hates non-alcoholic beer and what he likes most of all is football."
    Jacquie_stats = Jacquie(70, 12, Synopsis_Jacquie)
    print("Synopsis: ", Jacquie_stats.Synopsis)
    print("attack: ", Jacquie_stats.Attack)
    print("Defense: ", Jacquie_stats.DEF)

def stats_L():
    print("LOUIS")
    Synopsis_Louis = "Louis is an 30 years old married man" \
                           "It's easy to see that in life what he hates the most is poor people."
    Louis_stats = Louis(50, 30, Synopsis_Louis)
    print("Synopsis: ", Louis_stats.Synopsis)
    print("damage: ", Louis_stats.Attack)
    print("Defense: ", Louis_stats.DEF)


def stats_V():
    print("VLAD")
    Synopsis_Vlad = "Vlad is a young man aged of 17 yeards old who is dropping out school and is a drug dealer" \
                           "He hates the police and what he loves the most is addidas tracksuit"
    Vlad_stats = Vlad(150, 5, Synopsis_Vlad)
    print("Synopsis: ", Vlad_stats.Synopsis)
    print("damage: ", Vlad_stats.Attack)
    print("Defense: ", Vlad_stats.DEF)

def stats_E():
    print("ERICA")
    Synopsis_Erica = "a 35 year old with two children and a husband. " \
                     "She hates working overtime and likes promotions and savings."
    Erica_stats = Erica(75, 15, Synopsis_Erica)
    print("Synopsis: ", Erica_stats.Synopsis)
    print("damage: ", Erica_stats.Attack)
    print("Defense: ", Erica_stats.DEF)


def stats_S():
    print("STELLA")
    Synopsis_Stella = "a 22-year-old who lives with her boyfriend. " \
                      "She hates her parents and authority and loves going out with her friends on shopping trips."
    Stella_stats = Stella(60, 20, Synopsis_Stella)
    print("Synopsis: ", Stella_stats.Synopsis)
    print("damage: ", Stella_stats.Attack)
    print("Defense: ", Stella_stats.DEF)

def stats_Enfant():
    print("ENFANT")
    Synopsis_Enfant = ""
    Enfant_stats = Enfant(40, 50, Synopsis_Enfant)
    print("Synopsis: ", Enfant_stats.Synopsis)
    print("damage: ", Enfant_stats.Attack)
    print("Defense: ", Enfant_stats.DEF)

#Lancement du jeu première étape sélection des personnages
def selection_player():
    global player1, player2
    x = 0
    while x != 2:
        # On affiche les noms de chaque personnage sous forme de liste pour la sélection
        print("1.", "Bernard")
        print("2.", "Jacquie")
        print("3.", "Louis")
        print("4.", "Vlad")
        print("5.", "Erica")
        print("6.", "Stella")
        print("7.", "Mathéo")
        print("to select a character please enter a number")

        choix_pers = int(input())

        # Bernard
        if choix_pers == 1:
            stats_B()
            print("Do you want to take this character??")
            oui_non = input()
            if oui_non == "yes":
                if x == 0:
                    player1 = Bernard(100, 8, "siudlhk")
                    print("player 1 take Bernard")
                    print("player 2 select an other characters")
                    x = x + 1
                elif x == 1 and player1 != Bernard:
                    player2 = Bernard(100, 8, "siudlhk")
                    print("player 2 take Bernard")
                    x = x + 1
                elif player1 == Bernard:
                    print("take an other character")

            elif oui_non == "no":
                print("reselect")
            else:
                print(" Choose a character")

        # Jacquie
        elif choix_pers == 2:
            stats_J()
            print("voulez vous choisir ce personnage?")
            oui_non = input()
            if oui_non == "yes":
                if x == 0:
                    player1 = Jacquie(70, 12, "siudlhk")
                    print("player 1 take Jacquie")
                    print("player 2 select an other characters")
                    x = x + 1
                elif x == 1 and player1 != Jacquie:
                    player2 = Jacquie(70, 12, "siudlhk")
                    print("player 2 take Jacquie")
                    x = x + 1
                elif player1 == Jacquie:
                    print("take an other character")

            elif oui_non == "no":
                print("reselect")
            else:
                print(" Choose a character")

        # Louis
        elif choix_pers == 3:
            stats_L()
            print("Do you want to take this character??")
            oui_non = input()
            if oui_non == "yes":
                if x == 0:
                    player1 = Louis(50, 30, "siudlhk")
                    print("player 1 take Louis")
                    print("player 2 select an other characters")
                    x = x + 1
                elif x == 1 and player1 != Louis:
                    player2 = Louis(50, 30, "siudlhk")
                    print("player 2 take Louis")
                    x = x + 1
                elif player1 == Louis:
                    print("take an other character")

            elif oui_non == "no":
                print("reselect")
            else:
                print(" Choose a character")

        # Vlad
        elif choix_pers == 4:
            stats_V()
            print("Do you want to take this character??")
            oui_non = input()
            if oui_non == "yes":
                if x == 0:
                    player1 = Vlad(150, 5, "siudlhk")
                    print("player 1 take Vlad")
                    print("player 2 select an other characters")
                    x = x + 1
                elif x == 1 and player1 != Vlad:
                    player2 = Vlad(150, 5, "siudlhk")
                    print("player 2 take Vlad")
                    x = x + 1
                elif player1 == Vlad:
                    print("take an other character")

            elif oui_non == "no":
                print("reselect")
            else:
                print(" Choose a character")

        #Erica
        elif choix_pers == 5:
            stats_E()
            print("Do you want to take this character??")
            oui_non = input()
            if oui_non == "yes":
                if x == 0:
                    player1 = Erica(75, 15, "siudlhk")
                    print("player 1 take Erica")
                    print("player 2 select an other characters")
                    x = x + 1
                elif x == 1 and player1 != Erica:
                    player2 = Erica(75, 15, "siudlhk")
                    print("player 2 take Erica")
                    x = x + 1
                elif player1 == Erica:
                    print("take an other character")

            elif oui_non == "no":
                print("reselect")
            else:
                print(" Choose a character")

        #Stella
        elif choix_pers == 6:
            stats_S()
            print("Do you want to take this character??")
            oui_non = input()
            if oui_non == "yes":
                if x == 0:
                    player1 = Stella(60, 20, "siudlhk")
                    print("player 1 take Stella")
                    print("player 2 select an other characters")
                    x = x + 1
                elif x == 1 and player1 != Stella:
                    player2 = Stella(60, 20, "siudlhk")
                    print("player 2 take Stella")
                    x = x + 1
                elif player1 == Stella:
                    print("take an other character")

            elif oui_non == "no":
                print("reselect")
            else:
                print(" Choose a character")

        #Enfant
        elif choix_pers == 7:
            stats_Enfant()
            print("Do you want to take this character??")
            oui_non = input()
            if oui_non == "yes":
                if x == 0:
                    player1 = Enfant(40, 50, "siudlhk")
                    print("player 1 take Enfant")
                    print("player 2 select an other characters")
                    x = x + 1
                elif x == 1 and player1 != Enfant:
                    player2 = Enfant(40, 50, "siudlhk")
                    print("player 2 take Enfant")
                    x = x + 1
                elif player1 == Enfant:
                    print("take an other character")

            elif oui_non == "no":
                print("reselect")
            else:
                print(" Choose a character")


#on créer une liste

def New_game():
    print("welcome")
    print(" selected a character")
    # quand on appuie sur un perso afficher ses stats et laisser la possibiliter de valider ou de revenir à la sélection
    selection_player()
    combat()


def combat():
    H = True
    wwwwwww = randint(1, 2)
    while H == True:

        # attaque player 2
        if wwwwwww % 2 == 0:
            print("player 2")
            List_Sujets = ["you", "bro you", "you my friend", "mate you", "sweetie you", "honey you", "cutie you", "kitten you", "freak you"]
            List_Auxiliaires = ["are"]
            List_Verbes = ["annoying", "boring", "a chicken", "a morron", "a fool", "an old cow", "a smart ass", "a pain in the ass", "clingy"]
            List_Complements = ["it's insame", "don't you think ?", "it's so funny", "everyone is laughing at you", "for crying out loud", "hang in there", "go back to sleep", "pull yourself together", "but it suits you"]
            List_Liaisons = ["and", "after all", "besides", "in addition", "in reality", "or rather", "by the way", "also", "thereby"]
            List_Exclamations_finales = ["go to hell", "get lost", "i don't care", "piss off", "you look like a filthy person ", "you are repulsive", "you look like a potatoes", "you're slow", "you're smelling bad"]

            liste = []

            shuffle(List_Sujets)
            shuffle(List_Auxiliaires)
            shuffle(List_Verbes)
            shuffle(List_Complements)
            shuffle(List_Liaisons)
            shuffle(List_Exclamations_finales)

            #List_Sujets
            a = randint(1, 3)
            a1 = 0
            while a != a1:
                x = List_Sujets[a1]
                a1 = a1 + 1
                liste.append(x)

            #List_Auxiliaires
            b = 1
            b1 = 0
            while b != b1:
                x = List_Auxiliaires[b1]
                b1 = b1 + 1
                liste.append(x)
            b1 = 0
            while b != b1:
                x = List_Auxiliaires[b1]
                b1 = b1 + 1
                liste.append(x)

            #(List_Verbes
            c = randint(1, 2)
            c1 = 0
            while c != c1:
                x = List_Verbes[c1]
                c1 = c1 + 1
                liste.append(x)

            #List_Complements
            d = randint(1, 2)
            d1 = 0
            while d != d1:
                x = List_Complements[d1]
                d1 = d1 + 1
                liste.append(x)

            #list liaison
            e = randint(1, 3)
            e1 = 0
            while e != e1:
                x = List_Liaisons[e1]
                e1 = e1 + 1
                liste.append(x)

            #List_Exclamations_finales
            f = randint(1, 3)
            f1 = 0
            while f != f1:
                x = List_Exclamations_finales[f1]
                f1 = f1 + 1
                liste.append(x)


            shuffle(liste)
            omg = len(liste)
            choix = []
            z1 = 0
            while z1 < omg:

                #afficher les choix
                z = 0
                i = 1
                while z < len(liste):
                    print(i, ")", liste[z])
                    z = z + 1
                    i = i + 1

                print("sélectionné le mot(le chiffre) que vous voulez mettre")



                # afficher déplacer le nombre choisie dans une nouvelle liste
                choix_nombre = int(input()) - 1



                v = liste[choix_nombre]
                choix.append(v)
                liste.pop(choix_nombre)

                #afficher la liste de mot
                print("")
                d = ""
                for t in choix:
                    d += t + " "
                print(d)
                print("")

                # permet d'éffacer la liste choix
                print("vous pouvez suprimmer vos choix en appuyant tapant reset/"
                      "vous pouvez finir votre phrase(liste de chiffre) en tapant end")
                reset = input()
                if reset == "reset":
                    p = 0
                    while p < len(choix):
                        liste.append(choix[p])
                        p = p + 1
                    choix.clear()
                    z = 0
                elif reset == "end":
                    z1 = 1000000
                z1 = z1 + 1

            #compter les points

            i = 0
            while i < len(choix):
                test = choix[i]
                if test in List_Sujets:
                    choix[i] = 1
                elif test in List_Auxiliaires:
                    choix[i] = 2
                elif test in List_Verbes:
                    choix[i] = 3
                elif test in List_Complements:
                    choix[i] = 4
                elif test in List_Liaisons:
                    choix[i] = 5
                elif test in List_Exclamations_finales:
                    choix[i] = 6
                i = i + 1

            i = 0
            i1 = 1
            degat = 0
            while i1 < len(choix):
                calcul = choix[i1] - choix[i]

                i = i + 1
                i1 = i1 + 1
                if calcul == 1 or calcul == 5:
                    degat = degat + 10
                elif calcul < 1:
                    degat = degat - 5
                elif calcul > 1:
                    degat = degat - 5

            # dégat
            if degat > 0:

                player1.degat_subit((degat * player2.Attack) / 10)
                print(player1.DEF)
                wwwwwww = wwwwwww + 1
                if player1.DEF <= 0:
                    H = False
                    print("player 2 win ")
            elif degat < 0:
                player1.degat_subit(10)

                wwwwwww = wwwwwww + 1
                if player1.DEF <= 0:
                    print("player 1 loose")
                    H = False
            else:
                print("vous n'avez pas fait de dégats ce tour là")
        else:
            print("player 1")
            List_Sujets = ["you", "bro you", "you my friend", "mate you", "sweetie you", "honey you", "cutie you", "kitten you", "freak you"]
            List_Auxiliaires = ["are"]
            List_Verbes = ["annoying", "boring", "a chicken", "a morron", "a fool", "an old cow", "a smart ass", "a pain in the ass", "clingy"]
            List_Complements = ["it's insame", "don't you think ?", "it's so funny", "everyone is laughing at you", "for crying out loud", "hang in there", "go back to sleep", "pull yourself together", "but it suits you"]
            List_Liaisons = ["and", "after all", "besides", "in addition", "in reality", "or rather", "by the way", "also", "thereby"]
            List_Exclamations_finales = ["go to hell", "get lost", "i don't care", "piss off", "you look like a filthy person ", "you are repulsive", "you look like a potatoes", "you're slow", "you're smelling bad"]

            liste = []

            shuffle(List_Sujets)
            shuffle(List_Auxiliaires)
            shuffle(List_Verbes)
            shuffle(List_Complements)
            shuffle(List_Liaisons)
            shuffle(List_Exclamations_finales)

            #List_Sujets
            a = randint(1, 3)
            a1 = 0
            while a != a1:
                x = List_Sujets[a1]
                a1 = a1 + 1
                liste.append(x)

            #List_Auxiliaires
            b = 1
            b1 = 0
            while b != b1:
                x = List_Auxiliaires[b1]
                b1 = b1 + 1
                liste.append(x)
            b1 = 0
            while b != b1:
                x = List_Auxiliaires[b1]
                b1 = b1 + 1
                liste.append(x)

            #(List_Verbes
            c = randint(1, 2)
            c1 = 0
            while c != c1:
                x = List_Verbes[c1]
                c1 = c1 + 1
                liste.append(x)

            #List_Complements
            d = randint(1, 2)
            d1 = 0
            while d != d1:
                x = List_Complements[d1]
                d1 = d1 + 1
                liste.append(x)

            #list liaison
            e = randint(1, 3)
            e1 = 0
            while e != e1:
                x = List_Liaisons[e1]
                e1 = e1 + 1
                liste.append(x)

            #List_Exclamations_finales
            f = randint(1, 3)
            f1 = 0
            while f != f1:
                x = List_Exclamations_finales[f1]
                f1 = f1 + 1
                liste.append(x)


            shuffle(liste)
            omg = len(liste)
            choix = []
            z1 = 0
            while z1 < omg:

                #afficher les choix
                z = 0
                i = 1
                while z < len(liste):
                    print(i, ")", liste[z])
                    z = z + 1
                    i = i + 1

                print("sélectionné le mot(le chiffre) que vous voulez mettre")



                # afficher déplacer le nombre choisie dans une nouvelle liste
                choix_nombre = int(input()) - 1



                v = liste[choix_nombre]
                choix.append(v)
                liste.pop(choix_nombre)

                #afficher la liste de mot
                print("")
                d = ""
                for t in choix:
                    d += t + " "
                print(d)
                print("")

                # permet d'éffacer la liste choix
                print("vous pouvez suprimmer vos choix en appuyant tapant reset/"
                      "vous pouvez finir votre phrase(liste de chiffre) en tapant end")
                reset = input()
                if reset == "reset":
                    p = 0
                    while p < len(choix):
                        liste.append(choix[p])
                        p = p + 1
                    choix.clear()
                    z = 0
                elif reset == "end":
                    z1 = 1000000
                z1 = z1 + 1

            #compter les points

            i = 0
            while i < len(choix):
                test = choix[i]
                if test in List_Sujets:
                    choix[i] = 1
                elif test in List_Auxiliaires:
                    choix[i] = 2
                elif test in List_Verbes:
                    choix[i] = 3
                elif test in List_Complements:
                    choix[i] = 4
                elif test in List_Liaisons:
                    choix[i] = 5
                elif test in List_Exclamations_finales:
                    choix[i] = 6
                i = i + 1

            i = 0
            i1 = 1
            degat = 0
            while i1 < len(choix):
                calcul = choix[i1] - choix[i]

                i = i + 1
                i1 = i1 + 1
                if calcul == 1 or calcul == 5:
                    degat = degat + 10
                elif calcul < 1:
                    degat = degat - 5
                elif calcul > 1:
                    degat = degat - 5

            #dégat
            if degat > 0:

                player2.degat_subit((degat * player1.Attack)/10)
                print(player1.DEF)
                wwwwwww = wwwwwww + 1
                if player2.DEF <= 0:
                    H = False
                    print("player 1 win ")
            elif degat < 0:
                player2.degat_subit(10)

                wwwwwww = wwwwwww + 1
                if player2.DEF <= 0:
                    H = False
                    print("player 2 loose")
            else:
                print("vous n'avez pas fait de dégats ce tour là")



intro_titre()
