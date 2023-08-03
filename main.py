from colorama import Fore

def colorChange(color):
  if color == "r":
    print(Fore.RED, end="")
  elif color == " ":
    print("\033[0m", end="")
  elif color == "b":
    print(Fore.BLUE, end="")
  elif color == "y":
    print(Fore.YELLOW, end="")
  elif color == "g":
    print(Fore.GREEN, end="")
  elif color == "p":
    print(Fore.MAGENTA, end="")

  
userString = input("Enter a sentence to rainbow-izing?: ")
for letter in userString:
  colorChange(letter.lower())
  print(letter,end="")
print()
   