import random


def load_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words


def choose_word(words):
    return random.choice(words)


def validate_guess(guess, guessed_letters):
    if len(guess) != 1:
        print("הכנס תו אחד")
        return False
    elif guess in guessed_letters:
        print("הכנס שוב")
        return False
    return True


def update_word_state(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '*' for letter in word])


def play_game(words, num_players):
    scores = [0] * num_players
    player_turn = 0
    guessed_letters = set()

    while words:
        word = choose_word(words)
        words.remove(word)
        guessed_letters.clear()
        word_state = update_word_state(word, guessed_letters)

        print(f"המילה היא: {'*' * len(word)}")

        while '*' in word_state:
            print(f"זה הניחוש עד עכשיו: {word_state}")
            guess = input(f"שחקן {player_turn + 1}, הכנס אות: ").lower()

            if not validate_guess(guess, guessed_letters):
                continue

            guessed_letters.add(guess)

            if guess in word:
                scores[player_turn] += word.count(guess)
                print(f"האות {guess} קיימת במילה!")
            else:
                print(f"האות {guess} לא קיימת במילה!")
                player_turn = (player_turn + 1) % num_players

            word_state = update_word_state(word, guessed_letters)

        print(f"זו המילה: {word}")

    winner = scores.index(max(scores)) + 1
    print(f"המשחק הסתיים! השחקן עם הכי הרבה נקודות הוא שחקן {winner} עם {max(scores)} נקודות")


if __name__ == "__main__":
    words = load_words(r'C:\words.txt')
    num_players = int(input("כמה שחקנים משתתפים? "))
    play_game(words, num_players)
