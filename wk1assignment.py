print("Hello there!")
name=input("Enter your name:")
print("Hello to You "  + name)
age=input("Enter your age:")
print("You are " + age + " years old.")
favorite_color=input("Enter your favorite color:")
favorite_animal=input("Enter your favorite animal:")
piratename=" Miss fearless " + favorite_color + " " + favorite_animal
print("Your favorite color is " + favorite_color + " and your favorite animal is " + favorite_animal + ".")
print("Your pirate name is " + piratename + ".")
amount_of_gold_coins=input("Enter the amount of gold coins you have:")
print("You have " + amount_of_gold_coins + " gold coins.")
number_of_pirates_in_crew=input("Enter the number of pirates in crew:")
number_of_pirates_in_crew=int(number_of_pirates_in_crew)
amount_of_gold_coins=int(amount_of_gold_coins)
print("Each pirate will get " + str(amount_of_gold_coins // number_of_pirates_in_crew) + " gold coins.")
if amount_of_gold_coins // number_of_pirates_in_crew >= 15:
    print("Everyone is happy!")
else:
    print("Some of the pirates are unhappy!")
secret_number = 7
guess = input("Guess the secret number: ")

if int(guess) == secret_number:
    print("Nice! You did great")
else:
    print("Nahh! Nice try buddy but you are Wrong!")
word=input("Enter a word:")
print(word * 5)
Inventory=["Sword", "Compass", "Map", "Key", "Lantern"]
print(Inventory)

    



