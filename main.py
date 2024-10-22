# Programmers:  Hazel Osborne, Lucas Podowski
# Course:  CS151, Zelalem Yalew
# Due Date: 8/23/24
# Programming Assignment:  Lab 6
# Problem Statement: Calculates withdrawals, deposits, etc. like an ATM
# Data In: action choice, possibly deposit / withdrawal amount
# Data Out: balance
# Credits: Inspired from the Lab 5 answer key
# Purpose: To process banking information (like an ATM)

#Output Welcome message to explain purpose of the program
print("\n")
print("-*%*-" * 50)
print("Welcome to the ATM program! This program allows you to interact with your account balance.")
print("-*%*-" * 50 ,"\n")

#Name: user_choice_correction
#Parameter: none
#return: menu option
def user_choice_correction():
    user_choice = ''
#Prompt user to enter what they want to do at the ATM
    user_choice = str(input('Please enter D to deposit, W to withdraw, V to view balance, or E to exit: '))
    user_choice = user_choice.upper()
 #Error Check User Choice
    while user_choice != "E" and user_choice != "W" and user_choice != "V" and user_choice != "D":
        print ('Invalid Choice. Try Again')
        user_choice = str(input('Please enter D to deposit, W to withdraw, V to view balance, or E to exit: '))
        user_choice = user_choice.upper()
    return user_choice

#Name: invalid_amount
#parameter: amount
#return: amount
def invalid_amount(amount):
    while amount < 0:
        print("Invalid Input. Try Again")
        amount(input("Please enter your amount as a positive integer: "))
    amount = int(amount)
    return amount

#Name: deposit
#Parameter: current_balance
#Return: current_balance
def deposit(current_balance):
    deposit_amount = int(input("\n Please enter your deposit amount as a positive integer: "))
    #Error Checking Deposit amount
    invalid_amount(deposit_amount)
   #Calculating new balance
    current_balance = current_balance + deposit_amount
    return current_balance

#Name: withdraw
#parameter: current_balance
#return: balance
def withdraw(current_balance):
    withdraw_amount = int(input("\n Please enter your withdraw amount as a positive integer: "))
    #Error Checking withdraw amount
    invalid_amount(withdraw_amount)
    #Calculate new balance
    current_balance = current_balance - withdraw_amount
    #Check if warning interest statement should be displayed
    if current_balance < 0:
        print("Your balance is negative. You will be charged a 5% interest rate.")
    return current_balance

#Name: view_balance
#parameter: current_balance
#return: none
def view_balance(current_balance):
    print("Your current balance is: ", current_balance)
    return

#name: main
#parameter: none
#return: none
def main():
   balance = 1000
   (current_balance) = balance
   current_balance = int(current_balance)
   sentinel = "E"
#determing action
   user_choice = user_choice_correction()
#loop actions until user wants to exit
   while user_choice != sentinel:
        if user_choice == 'D':
            current_balance = deposit(current_balance)
        elif user_choice == "W":
            current_balance = withdraw(current_balance)
        elif user_choice == 'V':
           view_balance(current_balance)
        print("\n")
        print("-*%*-" * 50, "\n")
        user_choice = user_choice_correction()
   print ("\nThank you for using ATM program!")
   return

#Run main code
main()