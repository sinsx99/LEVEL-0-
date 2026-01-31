print("___ LIGHT SWITCH PROGRAM ___")

def light_switch():
    light_on =  False
    
    while True:
        print("\nCurrent Status:", "ON" if light_on else "OFF")
        user = input("Switch [ON/OFF] or [EXIT]: ").strip().lower()
        
        if user == "on":
            if light_on:
                print("Light was already ON")
            else: 
               light_on = True
               print("Light turned ON")
                
        elif user == "off":
            if not light_on:
                print("Light was already OFF")
            else:
               light_on = False
               print("Light turned OFF")
            
        elif user == "exit":
               print("Exiting light switch...")
               break
            
        else:
            print("Invalid input! Please use ON, OFF, or EXIT")

def main_menu():
    while True:
        light_switch()  # Run the light switch program
        
        restart = input("\nWould you like to use the light switch again? [Y/N]: ").strip().lower()
        if restart != 'y':
            print("\nThank you for using the Light Switch Program!")
            break

# Start the program
main_menu()