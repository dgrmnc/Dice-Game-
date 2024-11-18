import random
import time

# general fonc
def sleep(x):
    time.sleep(x)

# to get balance
def get_balance():
    balance = input("Welcome to the game.. How much would you like to deposit today?: $")
    if balance.isdigit():
        balance = int(balance)
        if balance >0 :
            print(f"Your current balance is now: {balance}")
            return balance
    else:
        print("Please enter a valid amount!")

# to ask for current spin round   
def dice_spin():
    while True:
        spin = input("Would you like to dice for this round(y / n , q to quit)?: ").lower()
        if spin == 'q':
            print("Exiting the game..")
            sleep(1.5)
            exit()
        elif spin == 'y':
            print("Let's see your bet then..")
            return True
        else:
            print("No Betting huh! Never forget that Do not roll the dice if you can't price!")    
            return False
        
# to get the bet
def get_bet(balance):
    max_bet = min(1000,balance)

    while True:
        bet = input("How much do you want to bet on?: $")
        if bet.isdigit():
            bet = int(bet)
            if 1 <= bet <= max_bet:
                return bet
            else:
                print(f"Your bet must be within the range: 1 - {max_bet}")
        else:
            print("Please enter a numeric value for betting..")

def get_bet_lines():

    max_lines = 5

    while True:
        line = input(f"How many lines you want to bet?(q to quit)(Max line is : {max_lines}): ")
        if line == 'q':
            print("Exiting the app...")
            sleep(0.5)
            exit()
        elif line.isdigit():
            line = int(line)
            if 1 <= line <= max_lines:
                return line
            else:
                print("Lines must be within the given range ")
        else:
            print("Please enter a valid number of line(s)")

# spinning result check
def spinning_of_dices(total_balance):
    print("Dicing...")
    sleep(1)
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print(f"{dice1}  | {dice2}")
        
    if dice1 == dice2:
        return True
    else:
        return False

# mainly check total balance after winning/losing
def game():
         total_balance = get_balance()
    
         while True:
            if not dice_spin():
                break
            
            bet = get_bet(total_balance)        
            line = get_bet_lines()
            total_bet = bet * line

            print(f"You placed a {line} line on your bet now you play with {total_bet}")

            if total_bet > total_balance:
                print(f"You can not bet more then you have in your pocket!\nWhat's in your pocket is ${total_balance}")
                continue

            if spinning_of_dices(total_bet):
                total_balance += total_bet
                print(f"Congrats man! You just won ${total_bet} and your current balance is ${total_balance}")
            else:
                total_balance -= total_bet
                print(f"You just lost ${total_bet} and your current balance is ${total_balance}")

            if total_balance <= 0:
                print("You are out of money man! Let's call it a day and just go home..")
            break

# to work it out
def main():
    game()

if __name__ == '__main__':
    main()
