import random

NUMBER_OF_DICE = 5
SIDES = 6
# The following constants can be used to describe the combination a player has.
FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIRS = 2
PAIR = 1
NOTHING = 0
RESULTSTRINGS = ["no special combination", "a pair", "two pairs", 
                 "three of a kind", "straight", "full house", 
                 "four of the kind", "five of the kind"]


# The function is used to initialize the random number generator.

def init_dice():
    seednumber = int(input("Enter a number to initialize the dice.\n"))
    random.seed(seednumber)
    
    
# The function returns a random number from interval 1-6 to give a 
# result of one throw of a dice.
    
def roll_dice():
    return random.randint(1, SIDES)


# The function rolls five dice and returns a list containing the figures of 
# the dice as integers.

def roll_all_dice():
    noppalista = []
    for i in range(NUMBER_OF_DICE):
        noppalista.append(roll_dice())
    return noppalista


# The function checks whether the list given as a parameter
# contains the same integer exactly 5 times. The function returns True, 
# if this is the case, and otherwise False.

def has_five_of_a_kind(noppalista):
    for figure in range(1, SIDES + 1):
        if noppalista.count(figure) == 5:
            return True
    return False


# The function checks whether the list given as a parameter
# contains the same integer exactly 4 times. The function returns True, 
# if this is the case, and otherwise False.

def has_four_of_a_kind(noppalista):
    for figure in range(1, SIDES + 1):
        if noppalista.count(figure) == 4:
            return True
    return False

   
# The function checks whether the list given as a parameter
# contains the same integer exactly 3 times. The function returns True, 
# if this is the case, and otherwise False.

def has_three_of_a_kind(noppalista):
    for figure in range(1, SIDES + 1):
        if noppalista.count(figure) == 3:
            return True
    return False


# The function checks whether the list given as a parameter
# contains the same integer exactly 2 times. The function returns True, 
# if this is the case, and otherwise False.

def has_pair(noppalista):
    for figure in range(1, SIDES + 1):
        if noppalista.count(figure) == 2:
            return True
    return False

def reroll(noppalista):
    print("Enter the numbers of the dice to be rerolled separated by a comma")
    print("or an empty line if you do not want to reroll.")
    mitka_nopat = input()
    if len(mitka_nopat) > 0:
        mitka_nopat1 = mitka_nopat.split(",")
        nopat_int = []
        for noppa in mitka_nopat1:
            noppa_lukuna = int(noppa)-1
            nopat_int.append(noppa_lukuna)
        toimiiko = acceptable(nopat_int)
        if toimiiko == True:
            for noppa in nopat_int:
                noppalista[noppa] = random.randint(1, SIDES)
                nopan_luku = noppa +1
                print("The new value for dice no {:d} is {:d}.".format(nopan_luku, noppalista[noppa]))
        if toimiiko == False:
            print("The numbers you entered break the rules of the game.")       
            print("No dice are rerolled.")
    return noppalista
def acceptable(numberlist):
    i = 0
    a = 0
    while i != len(numberlist):
        if 0 <= numberlist[i] <= 4:
            if i == 0:
                a += 1 
            else:        
                erotus = numberlist[i] - numberlist[i-1]
                if erotus != 0:
                    a += 1   
        i += 1
    if a == len(numberlist):
        return True
    else:
        return False
def has_straight(noppalista):
    q = noppalista[0]
    w = noppalista[1]
    e = noppalista[2]
    r = noppalista[3]
    t = noppalista[4]
    if  has_five_of_a_kind(noppalista) == False and  has_four_of_a_kind(noppalista) == False and  has_three_of_a_kind(noppalista) == False and  has_pair(noppalista) == False and q != 6 and w != 6 and e != 6 and r != 6 and t != 6:
        return True
    if  has_five_of_a_kind(noppalista) == False and has_four_of_a_kind(noppalista) == False and has_three_of_a_kind(noppalista) == False and has_pair(noppalista) == False and q != 1 and w != 1 and e != 1 and r != 1 and t != 1:
        return True
    else:
        return False
def has_full_house(noppalista):
    order = sorted(noppalista)
    if order[0] == order[1] == order[2] and order[3] == order[4]:
        return True
    if order[0] == order[1] and order[2] == order[3] == order[4]:
        return True    
    else:
        return False
def has_two_pairs(noppalista): 
    order = sorted(noppalista)
    if order[0] == order[1] and order[2] == order[3]:
        return True
    if order[0] == order[1] and order[3] == order[4]:
        return True
    if order[1] == order[2] and order[3] == order[4]:
        return True
    else:
        return False   
def check_combination(noppalista): 
    if has_five_of_a_kind(noppalista):
        return 7
    if has_four_of_a_kind(noppalista):
        return 6
    if has_full_house(noppalista):
        return 5
    if has_straight(noppalista):
        return 4
    if has_three_of_a_kind(noppalista):
        return 3
    if has_two_pairs(noppalista):
        return 2
    if has_pair(noppalista):
        return 1
    else:
        return 0
def main(): 
    init_dice() 
    noppalista = roll_all_dice()
    print("Your turn:")
    print("Your result is",noppalista)
    
    noppalista = reroll(noppalista)
 
    koneen_tulos=roll_all_dice()
    print("Your final result is ",noppalista)
    print("The result of the computer is", koneen_tulos)
    pelaaja = check_combination(noppalista)
    kone = check_combination(koneen_tulos)

    if pelaaja == 7:
        print("You have five of a kind.")
    if pelaaja == 6:
        print("You have four of a kind.")
    if pelaaja == 5:
        print("You have full house.")
    if pelaaja == 4:
        print("You have straight.")
    if pelaaja == 3:
        print("You have three of a kind.")
    if pelaaja == 2:
        print("You have two pairs.")
    if pelaaja == 1:
        print("You have a pair.")
    if pelaaja == 0:
        print("You have no special combination.") 
             
    if kone == 7:
        print("Computer has five of a kind.")
    if kone == 6:
        print("Computer has four of a kind.")
    if kone == 5:
        print("Computer has full house.")
    if kone == 4:
        print("Computer has straight.")
    if kone == 3:
        print("Computer has three of a kind.")
    if kone == 2:
        print("Computer has two pairs.")
    if kone == 1:
        print("Computer has a pair.")
    
    if kone == 0:
        print("Computer has nothing.")
        
    if pelaaja > kone: 
        print("You won.")
    if pelaaja == kone:
        print("You tied with computer.")
    if kone > pelaaja:
        print("Computer won.")
main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        