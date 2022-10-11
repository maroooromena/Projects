
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_lowercase1 = name1.lower()
name_lowercase2 = name2.lower()

letter_t = name_lowercase1.count("t") + name_lowercase2.count("t")
letter_r = name_lowercase1.count("r") + name_lowercase2.count("r")
letter_u = name_lowercase1.count("u") + name_lowercase2.count("u")
letter_e = name_lowercase1.count("e") + name_lowercase2.count("e")

letter_l = name_lowercase1.count("l") + name_lowercase2.count("l")
letter_o = name_lowercase1.count("o") + name_lowercase2.count("o")
letter_v = name_lowercase1.count("v") + name_lowercase2.count("v")

total_true = letter_t + letter_r + letter_u + letter_e
total_love = letter_l + letter_o + letter_v + letter_e

score = int(f"{total_true}{total_love}")

if score < 10 or score > 90:
 print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
 print(f"Your score is {score}, you are alright together.")
else:
 print(f"Your score is {score}")
