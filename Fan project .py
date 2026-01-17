from datetime import datetime



def update_fan(fan_on, mode, command):   
    if command == "on":
        fan_on = True
        mode = "manual"
        print("Fan forced ON")

    elif command == "off":
        fan_on = False
        mode = "manual"
        print("Fan forced OFF")

    elif command == "auto":
        mode = "auto"
        print("Automatic mode enabled") 

    if mode == "auto":
        hour = datetime.now().hour
        
        if hour >= 22 or hour < 7:
            fan_on = True
            print("Automatic: fan ON (night)")
        else:
            fan_on = False
            print("Automatic: fan OFF (daytime)")

    return fan_on, mode

fan_on = False
mode = "auto"

while True:
    command = input("Command (on/off/auto/status/exit): ").lower()
    
    if command == "exit":
        print("Shutting down fan controller.")
        break
 
    if command not in ("on", "off", "auto","status"):
        print("Unknown command")
    
    
    if command == "status":
        print("Mode:", mode)
        print("Fan is currently:", "ON" if fan_on else "OFF")
        continue

    
    fan_on, mode = update_fan(fan_on, mode, command)
    print("Fan is currently:", "ON" if fan_on else "OFF")


       
   