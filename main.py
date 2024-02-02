import random

MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000
ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolValue = {
    "A": 10,
    "B": 6,
    "C": 4,
    "D": 2
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol]* bet
            winningLines.append(line+1)
            
    return winnings, winningLines


def slotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):   #Rather than using a variable for iteration, we used underscore '_' as a iterator.
            allSymbols.append(symbol) 

    columns = []
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]   #[:] creates a copy rather than a reference which would've been created in its absence
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end =" | ")
            else:
                print(column[row], end ="")
        print()


def deposit():  #Function to handle the deposit functionality
    while(True):    #Infinite while-loop
        amount = input("What would you like to deposit: $")   #Initial deposit value input statement
        if (amount.isdigit()):  #Check before-hand for a valid number, as we will change the string input to integer each time, becuase by default, input() takes in strings. 
            amount = int(amount)    #Converting the string input to integer value
            if (amount > 0):    #If the entered value if a positive integer/greater than zero, break out of the infinite while-loop
                print(f"You have deposited ${amount}.\n")    #Print out deposited amount
                break   #break statement
            else:   #If amount less than or equal to zero 
                print("Enter a amount greater than zero.")   #Print out warning statement
        else:
            print("Please enter a valid number.")   #Print out warning statement

    return amount   #Return the input deposit amount


def getLines():
    while(True):    #Infinite while-loop
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")   #Initial lines input statement
        if (lines.isdigit()):  #Check before-hand for a valid number, as we will change the string input to integer each time, becuase by default, input() takes in strings. 
            lines = int(lines)    #Converting the string input to integer value
            if (MIN_LINES <= lines <= MAX_LINES):    #If the entered value if a positive integer/greater than zero, break out of the infinite while-loop
                print(f"You have bet on {lines} lines.\n")    #Print out deposited amount
                break   #break statement
            else:   #If amount less than or equal to zero 
                print(f"Enter valid number of lines between {MIN_LINES} and {MAX_LINES}")   #Print out warning statement
        else:
            print("Please enter a valid number.")   #Print out warning statement

    return lines   #Return the input deposit amount


def lineBet():
    while(True):    #Infinite while-loop
        amount = input("What would you like to bet on each line: $")   #Bet for each slot line input statement
        if (amount.isdigit()):  #Check before-hand for a valid number, as we will change the string input to integer each time, becuase by default, input() takes in strings. 
            amount = int(amount)    #Converting the string input to integer value
            if (MIN_BET <= amount <= MAX_BET):    #Checking for appropriate value within defined bounds
                print(f"You have bet ${amount} on each line.\n")    #Print out amount to bet per line
                break   #break statement
            else:   #If amount not within bounds
                print(f"Enter an amount between ${MIN_BET} and ${MAX_BET}")   #Print out warning statement
        else:
            print("Please enter a valid number.")   #Print out warning statement

    return amount  #Return the input deposit amount


def spin(balance):
    lines = getLines()  #Create a variable holding the value returned from the "getLines()" function
    
    while(True):
        bet = lineBet()   #Create a variable holding the value returned from the "lineBet()" function
        totalBet = bet*lines
        if (totalBet <= balance):
            break
        else:
            print("Total bet exceeded the account balance.")
    
    print(f"\nYou have a balance of ${balance}.\nYou are betting ${bet} on {lines} lines.\nTotal bet is equal to ${totalBet}.")
    
    slots = slotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)

    winnings, winningLines = checkWinnings(slots,lines,bet,symbolValue)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winningLines)
    
    return winnings - totalBet


def main():
    balance = deposit()   #Create a variable holding the value returned from the "deposit()" function
    while(True):
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play slots (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}!")


main()