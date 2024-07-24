print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

t = name1_lower.count("t") + name2_lower.count("t")
r = name1_lower.count("r") + name2_lower.count("r")
u = name1_lower.count("u") + name2_lower.count("u")
e = name1_lower.count("e") + name2_lower.count("e")

l = name1_lower.count("l") + name2_lower.count("l")
o = name1_lower.count("o") + name2_lower.count("0")
v = name1_lower.count("v") + name2_lower.count("v")
e = name1_lower.count("e") + name2_lower.count("e")

true = t + r + u + e
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}. You're not cappable of being together.")
   