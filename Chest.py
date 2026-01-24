#adventurer finds type chest he gets type items


def item_drop():
    chest_data = {
        "gold": "1234",
        "platinum": "1242", 
        "bronze": "0000"
    }
   
    found_chest = input("You have found 3 chests,You can only choose one, gold/platinum/bronze: ").lower().strip()
    
    if found_chest  not in chest_data:
        print("Chest not Found /Exiting")
        return

    print(f"You have choosen {found_chest} This chest is locked!") 


    chest_lock = input("Enter 4 digit Code to Unlock this chest :").lower().strip()

    if chest_lock == chest_data[found_chest]:
        if found_chest == "gold":
            print("Unlocked! You earned Gold Armor!")
        elif found_chest == "platinum":
            print("Unlocked! You earned a Silver Sword!")
        elif found_chest == "bronze":
            print("Unlocked! You earned a Silver Sword!")    
        else:
            print("Unlocked! You earned 5 gold coins!")
    else:
        print("Incorrect code. Exiting.")


item_drop()
