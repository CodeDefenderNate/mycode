#!/usr/bin/ python3

choose = "Weigh thy considerations with great care and elect thine Champion wisely!:"
A = "Mage: Magick, Staff and Light Armor"
B = "Warrior: Melee, Sword and Shield"
C = "Thief: Melee, Daggers and Light Armor"
D = "Archer: Ranged, Bow and Arrow"

title = "Welcome to Dragon's Dogma II! Who will you choose?"
lines = "*"*50

def show_menu():
    print(lines)
    print(title)
    print(lines)
    
def Mage():
    print("The Mage is a powerful ally who specializes in the use of magick offerring enchanments, heals, and attacks to aid their party...")

def Warrior():
    print("Warriors are hulkin brutes specializing in the use of two-handed weapons capable of devestating groups of enemies...")

def Thief():
    print("The thief is a shifty one who focuses on speed and stealth to quickly deal with foes using daggers...")

def Archer():
    print("The Archer is a long-ranged specialist who excells with bow and arrow...")

def main():
    show_menu()
    choice = input(f"{choose}\n A: {A}\n B: {B}\n C: {C}\n D: {D}\nEnter your selection: ").lower()
    if choice == "a":
        print(Mage())
    elif choice == "b":
        print(Warrior())
    elif choice == "c":
        print(Thief())
    else:
        print(Archer())

if __name__ == "__main__":
    main()