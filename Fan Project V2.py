import time
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

    return fan_on, mode


def auto_tick(fan_on, mode):
    if mode == "auto":
        hour = datetime.now().hour

        if hour >= 22 or hour < 7:
            fan_on = True
        else:
            fan_on = False
    return fan_on


def log_state_change(prev_fan, prev_mode, fan_on, mode):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if prev_fan != fan_on:
        print(f"[{timestamp}] Fan turned {'ON' if fan_on else 'OFF'}")

    if prev_mode != mode:
        print(f"[{timestamp}] Mode changed to {mode.upper()}")


fan_on = False
mode = "auto"


print("Fan controller started")
print("Night mode: ON from 10 PM to 7 AM")
print("---------------------------------")


try:
    while True:
        command = input("Command (on/off/auto/status/exit): ").lower()
    
        if command == "exit":
            print("Shutting down fan controller.")
            break

        if command == "status":
            print("Mode:", mode)
            print("Fan is currently:", "ON" if fan_on else "OFF")
            continue

        if command not in ("on", "off", "auto"):
            print("Unknown command")
            continue
        
        prev_fan = fan_on
        prev_mode = mode


        fan_on, mode = update_fan(fan_on, mode, command)
    
        fan_on = auto_tick(fan_on , mode)
    
    
        log_state_change(prev_fan, prev_mode, fan_on, mode)

        print("Fan is currently:", "ON" if fan_on else "OFF")
        time.sleep(60)

except KeyboardInterrupt:
    print("\nEmergency stop. Controller halted.")
    