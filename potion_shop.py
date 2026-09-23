health_potion = 50
mana_potion = 20
gold = 100
print("Hey there! Ive got 2 potions, choose between 1 or 2.")
print("1: The Health Potion, 50 Gold")
print("2: The Mana Potion, 20 Gold")
which = 3
while which < 1 or which > 2:
    which = int(input("Which one would you like? "))
    if which == 1:
        amount = 0
        while amount <= 0:
            amount = int(input("How many of those would you like? "))
        affordable = gold - amount*health_potion
        if affordable < 0:
            while affordable < 0:
                   broke = 0
                   while broke <= 0:
                       broke = int(input("You dont have enough gold for that, how many would you like? "))
                   affordable = gold - broke*health_potion
            gold = gold - broke*health_potion
            print("Here you are! +", broke, "Health Potions")
        elif affordable >= 0:
            gold = gold - amount*health_potion
            print("Here you are! +", amount, "Health Potions")
    if which == 2:
       amount2 = 0
       while amount2 <= 0:
           amount2 = int(input("How many of those would you like? "))
       affordable2 = gold - amount2*mana_potion
       if affordable2 < 0:
           while affordable2 < 0:
               broke2 = 0
               while broke2 <= 0:
                   broke2 = int(input("You dont have enough gold for that, how many would you like? "))
               affordable2 = gold - broke2*mana_potion
           gold = gold - broke2*mana_potion
           print("Here you are! +", broke2, "Mana Potions")
       elif affordable2 >= 0:
           gold = gold - amount2*mana_potion
           print("Here you are! +", amount2, "Mana Potions")