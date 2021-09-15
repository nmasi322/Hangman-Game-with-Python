import random
import time

print('Welcome to Hangman Game by Edeh DivineFavour')
name = input("Enter your name: ")
print('Hey there, ' + name + '! Best of Luck!')
time.sleep(2)
print('The game is about to start... \n'
      'Lets play Hangman!')
time.sleep(3)
print('These are the words to guess from: '
      'book, monday, movie, promise, kids, adults, lungs, doll, rhyme, damage, heart, plants, film')


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ['book', 'monday', 'movie', 'promise', 'kids', 'adults', 'lungs', 'doll', 'rhyme',
                      'damage', 'heart', 'plants', 'film']
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ''


def play_loop():
    global play_game
    play_game = input('Do you want to play again? y = yes and n = no: ')
    if play_game == 'y':
        main()
        hangman()
    elif play_game == 'n':
        print('Thanks for playing! We expect you back again!')
        exit()
    else:
        print('Invalid entry')


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5

    guess = input('Enter a word from above: ' + display + " Enter your guess: ")
    guess = guess.strip()
    if len(guess.strip()) == 0:
        print("Invalid input, Try a letter more than two words please...")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print('Try another letter.\n')
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess. ' + str(limit - count) + 'Guesses remaining\n')
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess. ' + str(limit - count) + 'Guesses remaining\n')
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess. ' + str(limit - count) + 'Guesses remaining\n')
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess. ' + str(limit - count) + 'Last guess remaining\n')
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print('Wrong guess. You are hanged!!!!\n')
            print('The word was:',already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats you got the word correctly!")
        play_loop()
    elif count != limit:
        hangman()

main()

hangman()


