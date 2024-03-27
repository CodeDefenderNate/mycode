marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "power": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "power": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "power": "super strength",
  "archenemy": "adrenaline"}
             }

def main():

    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")
    char_stat = input("What statistic do you want to know about? (real name, power, archenemy)")

    print(f"{char_name}'s {char_stat} is: {marvelchars.get(char_name).get(char_stat).title()}")

main()