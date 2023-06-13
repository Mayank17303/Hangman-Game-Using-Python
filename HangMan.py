import random

stages = ['''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
         ========
          ''','''
          +---+
          |   |
          O   |
         /|\  |
         /    |
         ========
          ''','''
          +---+
          |   |
          O   |
         /|\  |
              |
         ========
          ''','''
          +---+
          |   |
          O   |
         /|   |
              |
         ========
          ''','''
          +---+
          |   |
          O   |
          |   |
              |
              |
         ========
          ''','''
          +---+
          |   |
          O   |
              |
              |
              |
         ========
          ''','''
          +---+
          |   |
              |
              |
              |
              |
         ========
          ''']

word_list = [
    "absence",
    "abuse",
    "account",
    "accident",
    "beneath",
    "bend",
    "benefit",
    "biology",
    "bitter",
    "candidate",
    "campaign",
    "camera",
    "capacity",
    "capture",
    "deaf",
    "daughter",
    "deal",
    "decorate",
    "dialogue",
    "economy",
    "finance",
    "educate",
    "efficient",
    "supportive",
    "elderly",
    "flight",
    "folk",
    "flame",
    "frustration",
    "garbage",
    "gather",
    "gentle",
    "global",
    "hilarious",
    "intelligence",
    "jazz",
    "knife",
    "longevity",
    "momument",
    "nonsense",
    "nobody",
    "turmeric",
    "utilize",
    "sashimi",
    "reconfigure",
    "wheat",
    "yellowish",
    "zone",
]


chosen_word = random.choice(word_list)

lives = 6
 
print(f"Choosen word is {chosen_word}")
# print(chosen_word)
display = []
for letter in chosen_word:
    display += "_"

# print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a word : ").lower()

    # print(guess)

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(display)
    
    if guess not in chosen_word :
        lives -= 1    
        if lives == 0 :
            end_of_game = True
            print("\n\n💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀")
            print("💀💀💀💀💀💀 Game Over 💀💀💀💀💀💀💀")
            print("💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀")


    if "_" not in display:
        end_of_game = True
        print("\n\n✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")
        print("✅✅✅✅✅✅✅ You won ✅✅✅✅✅✅✅✅✅✅✅")
        print("✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")

    print(stages[lives])
