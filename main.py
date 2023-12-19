import pyautogui
import time
import keyboard
import os

count = 0
lines = []

#No Bitches
#pyinstaller --onefile "C:\Users\Painf\OneDrive\Desktop\VS Code\CodeRaiding\CodeRaidingTool.py"
def on_key_event(e):
    global count
    int(count)
    if e.name == ']' and e.event_type == 'down':
        if count < len(lines):
            line = lines[count].strip() 
            print("[" + "{:04}".format(count+1) +"]ENTERING:" + lines[count],end='')
            pyautogui.typewrite(line, interval=0.1)
            count += 1
        else:
            print("All codes tested :(")

def main():
    global count
    print("Press 'ctrl+c' to exit.")
    text = input("[1]Start from top\n[2]Start from specified code count\n[3]Split codes between x players\n")
    text = text.lower()
    if text == '1' or text == '2' or text == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        if(text == '1'): count = 0
        elif(text == '2'): 
            count = int(input("What was the last code count you entered(NOT the last code you entered):"))
            if(count != 0): print("Previous ~ [" + "{:04}".format(count) +"]ENTERED:" + lines[count-1],end='')
        else:
            totalPlayers = int(input("How many players:"))
            section = int(input(f"Codes are split between {totalPlayers} sections, which section are you taking(1-{totalPlayers}):"))-1
            total_codes = len(lines)
            codes_per_section = total_codes // totalPlayers
            if(section != totalPlayers): print(f"Your codes ~ [{((section)*codes_per_section)+1}-{((section)*codes_per_section+codes_per_section-1)+1}]")
            else: print(f"Your codes ~ [{((section)*codes_per_section)+1}-{len(lines)}]")
            count = ((section)*codes_per_section)+1

        print("Tool Active...")

        keyboard.hook(on_key_event)

        try:
            while True:
                time.sleep(.1)
        except KeyboardInterrupt:
            pass
        finally:
            keyboard.unhook_all()
    else:
        input("Invalid Input(Enter)")
        main()

# Read file content into a list of lines
with open('codes.txt', 'r') as file:
    lines = file.readlines()

if __name__ == "__main__":
    main()