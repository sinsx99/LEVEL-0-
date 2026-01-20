import time
from datetime import datetime


#behavior functions

def update_door(locked, mode, command):
    if command == "lock":
        locked = True
        mode ="manual"
        print("Door locked manually")
    
    elif command == "unlock":
        locked = False
        mode = "manual"
        print("Door unlocked manually")

    elif command == "auto":
        mode= "auto"
        print("Automatic mode enabled")

    return locked, mode

def auto_tick(locked, mode):
    if mode == "auto":
        hour = datetime.now().hour

        
        if hour >= 22 or hour < 7:
            locked = True
        else:
            locked = False 
        
    return locked


def log_state_change(prev_locked, prev_mode, locked, mode):
    pass


#state

locked = True
mode = "auto"


print("Door controller started")
print("-------------------------")


#control loop

try:
    while True:
        command = input("Command (lock/unlock/auto/status/exit)").lower()

        if command == "exit":
            print("Shutting down door controller.")
            break

        if command == "status":
            print("Mode", mode)
            print("Door is currently", "LOCKED" if locked else "UNLOCKED")
            continue
        
        if command not in ("lock", "unlock", "auto"):
            print("Unknown command")
            continue

        #snapshot state 
        prev_locked = locked
        prev_mode = mode

#apply command function called into while loop
        locked, mode = update_door(locked, mode, command)

#automatic behavior function called into while loop
        locked = auto_tick(locked, mode)

#observe
        log_state_change(prev_locked, prev_mode, locked, mode)

        print("Door is currently:", "LOCKED" if locked else "UNLOCKED" )
        time.sleep(0)

except KeyboardInterrupt:
    print("\nEmergency stop. Controller halted.")