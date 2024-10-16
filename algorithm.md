# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Output welcome message to explain the purpose of the program.
2. Name: user_choice
   * Parameter: none
   * return: menu option
   * Algorithm:
     1. define choice as an empty string
     2. prompt user to enter what they want to do at the ATM: "Please enter D to deposit, W to withdraw, V to view balance, 
     or E to exit", store as choice
     3. case correct the choice to uppercase
     4. while choice is not 'D' 'W' 'V' or "E"
        1. output invalid choice: 'Invalid choice try again'
        2. prompt user to re-enter their choice: "Please Enter D to deposit, W to withdraw, V to view balance, 
     or E to exit" store as choice
        3. case correct to uppercase
3. Name: Deposit
   * Parameter: balance
   * Return: balance
   * Algorithm:
     1. Prompt user to enter how much they would like to deposit in $ stored as deposit amount
     2. while deposit amount is not digit
        1. output invalid amount
        2. prompt user to enter deposit amount: "Please enter your deposit amount as a number." store as deposit amount
     3. store deposit amount as a float
     4. add deposit amount from the balance
4. Name: withdraw
    * parameter: balance
    * return: balance
    * algorithm:
      1. prompt user to enter the amount they would like to withdraw, store as withdrawal amount
      2. while withdraw amount is not digit
         1. output invalid amount
         2. prompt user to enter withdraw amount: "Please enter your withdrawal amount as a number." store as deposit amount
      3. store withdrawal amount as a float
      4. subtract withdrawal amount from the balance
      5. check if balance is < 0
         1. output: "Your balance is negative. You will be charged a 5% interest rate"
5. Name: view_balance
    * parameter: balance
    * return: none
    * algorithm:
      1. output balance: "Your current balance is: $"
6. name: main
    * parameter: none
    * return: none
    * algorithm:
      1. set initial balance to 0
      2. set SENTINEL as 'E'
      3. call the user_choice function
      4. while user_choice is not SENTINEL
         1. check if user_choice is 'D'
            1. call deposit
         2. Otherwise if user_choice is 'W'
            1. call withdraw
         3. Otherwise if User_choice is 'V'
            1. call view_balance
         4. call user_choice
      5. output a message indicating theATM program has ended.