# Funciton to generate random 4-digit number with unique digits
# Function to calculate cows, bulls for a given guess
# Function main to play the game

import random

# Function to generate a random 4-digit number with unique digits
def generate_secret():
  secret = list(range(10))
  random.shuffle(secret)
  return ''.join([str(digit) for digit in secret[:4]])


def calculate_cows_and_bulls(secret, guess):
  bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
  cows = 0 # Initliali the number of cows
  secret_counts = {}
  guess_counts = {}

  for i in range(4):
    if guess[i] != secret[i]:
      if secret[i] in secret_counts:
        secret_counts[secret[i]] += 1
      else:
        secret_counts[secret[i]] = 1
      if guess[i] in guess_counts:
        guess_counts[guess[i]] += 1
      else:
        guess_counts[guess[i]] = 1

  return cows, bulls



# User will guess the number and program will tell the number of cows and bulls
# If the user guesses the number correctly, the program will provide a congratulatory message
# If the user enters an invalid guess, the program will ask the user to enter a valid guess
# the game will continue until the user guesses the number correctly

def main():
  secret = generate_secret()
  print('I have generated a 4-digit number with unique digits. Try to guess it!')

  while True:
    guess = input('Guess: ')
    if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
      cows, bulls = calculate_cows_and_bulls(secret, guess)
      print(f'{cows} cows, {bulls} bulls')

      if bulls == 4:
        print('Congratulations! You guessed the correct number')
        break
    else:
      print('Invalid guess. Please enter a 4-digit number with unique digits.')
      
      
if __name__ == '__main__':
    main()