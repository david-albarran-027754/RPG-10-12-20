import random

'''
Living in 2020, a Karen has woken up and tries to get rid of face masks.
Karen goes to a Walmart and fights all the customers with masks.
Karen can use weapons and armor, and has multiple abilities:
"Conspiracy Theory", "Mask Grab", "Yell and Throw", or "Run"
These abilities have a chance to hit or miss, Karen can level up. 
'''


kHealth = 5

#--------------- Looting System ----------------

chest = [1,5,10,15,20]
loot = False
inv = []

expHealth = 0
RealHealth = kHealth + expHealth
RealHealthE = kHealth + expHealth
rh = [RealHealth, RealHealthE]



def RealHealthy(i):
    RealHealthE + 5
    if RealHealthE <= RealHealth:
        return RealHealth
    else:
        return RealHealth


def lootcon(kList, loot, rh):
    openloot = input("Open Chest? 'y' or 'n'. >> ")
    if openloot == "y":
        loot = True
    elif openloot == "n":
        print("  You have chosen to skip loot, so you will be healed. ")
        RealHealthE = RealHealth + 5
        print("  Your Health went from ", RealHealth, "to ", RealHealthy(5), ". ")

    else:
        print("  Invalid response. Input fixed to 'n'. ")
        
    #item draws
    if loot == True:
        melee = ["Frozen Turkey: +7 Melee",
                 "Eggs: +2 Range",
                 "Water: +1 Range" ,
                 "Baguette: +5 Melee",
                 "Soda and Mentos: +4 Range",
                 "Thawed Out Wings: +3 Range"]
        meleecpu = random.choice(melee)
        
        
        armor = ["Tin Foil Hat: +5 Armor", "Watermelon Helmet: +3 Armor"]
        armorcpu = random.choice(armor)
        #CPU picks Melee or Armor Equipment.
        pool = [meleecpu, armorcpu]

        lootdrop = random.choice(pool)
        if lootdrop == meleecpu:
            #Adds weapon values to character.
            if meleecpu == "Frozen Turkey: +7 Melee":
                kList[KMELEE] += 7
                
            elif meleecpu == "Eggs: +2 Range":
                kList[KRANGE] += 2
            elif meleecpu == "Water: +1 Range":
                kList[KRANGE] += 1
            elif meleecpu == "Baguette: +5 Melee":
                kList[KMELEE] += 5
            elif meleecpu == "Soda and Mentos: +4 Range":
                kList[KRANGE] += 4
            elif meleecpu == "Thawed Out Wings: +3 Range":
                kList[KRANGE] += 3
                
        else:
            #Adds Armor values to character.
                if armorcpu == "Tin Foil Hat: +5 Armor":
                    kList[KARMOR] += 5
                elif armorcpu == "Watermelon Helmet: +3 Armor":
                    kList[KARMOR] += 3



        
        print(" ", lootdrop)

        #Does the user want this.
        invcheck = input(" Do you want this? 'y' or 'n' >>")
        if inv[0] in inv:
                inv.remove[0]
        if invcheck == "y":
            
                inv.append(lootdrop)
                print(inv)
            
        else:
            print("Item not received." )



#--------------------------------------------------------------------
kArmor = 1
kArmorE = 1
kMelee = 1
kMeleeE = 1
kRange = 1
kRangeE = 1

kExp = 0
#----------------------- Reward system ------------------------------
def prize(eHealth, eAttack, eArmor, kExp):
    kExp = eHealth + eAttack
    print(kExp)
    print("You have received", kExp, " Experience. ")
    bonus = input("You can increase one of your stats. Upgrade 'melee', 'armor', 'health'.")
    if bonus == "melee":
          kList[KMELEE] += 1
          print("Melee has increased from", kList[KMELEE] - 1,
                "to", kList[KMELEE], ". ")

#---------Ending---------
def end():
    print("You have fought valiantly, but their logic overpowered you. Now you must go home ashamed.")
    sys.exit("Maybe try talking to the manager instead of fighting customers next time. ")



#--------------- Fighting System ---------------
    #A Bunch of values

KRANGE = 0
KMELEE = 1
KARMOR = 2
KHEALTH = 3
#          0       1       2       3
kList = [kRange, kMelee, kArmor]

playerpos = 1
Rounds = 0


cMelee = 1
cRange = 1


eHealth = random.randint(5,10)
eHealthE = random.randint(5,10)
eAttack = random.randint(1,5)
eArmor = 1

print(" Your Health is ", kHealth)
print(" Your Attack is ", kList[KMELEE])

print("")
print("------------")
lootcon(kList, loot, rh) #kRange, kMelee, kArmor
print("DEV TXT: Health:", kHealth)
print("  Developer Troubleshoot Text:", "Melee:", kList[KMELEE], "Armor:", kList[KARMOR], "Range:", kList[KRANGE]) #kMelee, kArmor, kRange
print("------------")
print("")

def Fight(eHealth, eAttack, kList, eArmor, kHealth, Rounds):
    Running = True
    while Running:
        


        
        print(" Karen has encountered a customer. They have",
                eHealth,
                "Points of Health and",
                eAttack,
                "Points of Attack,",
                )
        #User chooses wheither to fight or not.
        fight = input("Fight? 'y' or 'n'. >> ")
        if fight == "y":
            combat = True
        if fight == "n":
            break

        #User chose to fight.
        while combat:
            if eHealth <= 0:
                Running = False
                break
            if kHealth <= 0:
                end()
            
            #Karens move set.
            print("1: Mask Grab. (Does Melee Damage)")
            print("2: Yell and Throw. (Does Range Damage)")
            print("3: Conspiracy Theory. (Random Chance to instantly defeat opponent.)")
            strat = input("Type the number corroesponding to the attack. >> ")
            #If Karen chose to Mask Grab
            if strat == "1":
                kfight = kList[KMELEE] / eArmor
                print(kList[KMELEE], eArmor)
                eHealth = eHealth - kfight

                print(eHealth)
                print("  Enemy has taken ", kfight, " damage. ")
                print("  Enemy has ", eHealth, " Health left. ")

            #If Karen chose to Yell and Throw.
            elif strat == "2":
                kFight = kList[KRANGE] / eArmor
                print(kList[KRANGE], eArmor)
                eHealth = eHealth - kFight
                print(eHealth)
                print("  Enemy has taken ", kFight, " damage. ")
                print("  Enemy has ", eHealth, " Health left. ")
            
            print("")
            #Enemy Attack
            eAttackE = eAttack - kList[KARMOR]
            if eAttackE <= -1:
                eAttackE = 0
            print("DEV TXT: ", eAttackE)
            kHealth = kHealth - eAttackE
            
            print("  Karen has taken ", eAttackE, " damage.")
            print("  Karens armor has reduced enemy damage by", kList[KARMOR], ". ")
            print("  Karen has ", kHealth, " Health left.")

            

            #Round Number and End
            Rounds = Rounds + 1
            print("Round: ", Rounds)
            combat = True
            print("")
            print("------")
Fight(eHealth, eAttack, kList, eArmor, kHealth, Rounds)

prize(eHealth, eAttack, eArmor, kExp)

lootcon(kList, loot, rh)

print("hi")
