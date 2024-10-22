# Algorithm Document


1. Output welcome message to explain the purpose of the program.
2. Name: user_choice_correction
3. Parameter: none
4. return: menu option
5. Algorithm:
   1. define choice as an empty string
   2. prompt user to enter what they want to do at the ATM: "Please enter D to deposit, W to withdraw, V to view balance,
      or E to exit", store as choice
   3. case correct the choice to uppercase
   4. while choice is not 'D' 'W' 'V' or "E"
      1. output invalid choice: 'Invalid choice try again'
      2. prompt user to re-enter their choice: "Please Enter D to deposit, W to withdraw, V to view balance,
         or E to exit" store as choice
      3. case correct to uppercase
   5. return user_choice
6. Name: invalid_amount 
7. parameter: amount
8. return: amount
9. algorithm:
   1. while amount is not digit
      1. output invalid amount statement
      2. prompt user to enter deposit amount: "Please enter your amount as an integer." store as deposit amount
   2. return amount

10. Name: deposit
11. Parameter: current_balance
12. Return: current_balance
13. Algorithm:
    1. Prompt user to enter how much they would like to deposit in $ stored as deposit amount
    2. call invalid_amount
    3. add amount to the current_balance
    4. return current_balance
14. Name: withdraw
15. parameter: current_balance
16. return: current_balance 
17. algorithm:
    1. prompt user to enter the amount they would like to withdraw, store as withdrawal amount
    2. call invalid_amount
    3. subtract amount from the current_balance
    4. check if current_balance is < 0
        1. output: "Your balance is negative. You will be charged a 5% interest rate"
    5. return current_balance
        
18. Name: view_balance
19. parameter: current_balance
20. return: none
21. algorithm:
    1. output balance: "Your current balance is: $"
    2. return
22. name: main 
23. parameter: none 
24. return: none 
25. algorithm:
    1. set  balance to 1000
    2. set SENTINEL as 'E'
    3. call the user_choice_correction function
    4. while user_choice is not SENTINEL
       1. check if user_choice is 'D'
          1. call deposit
          2. Otherwise, if user_choice is 'W'
             1. call withdraw
             2. Otherwise, if User_choice is 'V'
                1. call view_balance
             3. call user_choice
    5. output a message indicating theATM program has ended.
    6. return
26. Call Main function