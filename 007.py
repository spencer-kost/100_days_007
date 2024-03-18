#007.py Hangman Game
import random
import ascii # type: ignore
with open('words.txt', 'r') as file:
    words = file.read().split()

#characters = int(input("How many letters do you want your word to be? (3-10 letters)\n"))

answer = random.choice(words)
answer_list = [char for char in answer]
guess = ["*"] * len(answer)

lives = 5

print(f"Your word has ",len(answer)," characters.")
print(guess)
old_guess = []
print(answer_list)

while answer_list != guess and lives >=0:
    last_guess  = input("Guess a letter:\n").lower()
    if last_guess in answer_list:
        if last_guess in guess:
            print(f"You already guessed",last_guess,". You have ",lives+1," guesses left.")
            print(guess)
            print(ascii.hangmanpics[5-lives])
        else:
            print(f"Correct!",last_guess,"is in the word. You have ",lives+1," guesses left.")
            index = 0
            for ii in answer_list:
                if ii == last_guess:
                    guess[index] = last_guess
                index += 1
            print(guess)
            print(ascii.hangmanpics[5-lives])
    else:
        if last_guess in old_guess:
            print(f"You already guessed",last_guess,". Try again. You have ",lives+1," guesses left.")
            print(guess)
            print(ascii.hangmanpics[5-lives])
        else:
            lives += -1
            print(f"You guessed wrong,",last_guess,"is not in the word. you have ",lives+1," guesses left.")
            print(guess)
            print(ascii.hangmanpics[5-lives])
    old_guess.append(last_guess)

if answer_list == guess and lives>=0:
    print(f"Congragulations, you won! And you had ",lives+1," guesses left.")
else:
    print(f"Looks like you lost... Should have guessed better!")


# print(answer)
