def ATM():
    print('Welcome! Please insert your card.')

    # Input and validate PIN
    while True:
        try:
            pin = int(input('Enter PIN: '))
            break
        except ValueError:
            print('Invalid input. Please enter a numeric PIN.')

    if pin == 4567:
        print('Welcome, Mr. Adeniji!')
    else:
        print('Invalid PIN. Exiting...')
        return

    # Menu for transactions
    print('What transaction would you like to perform?')
    print('Transfer (T)')
    print('Deposit (D)')
    print('Withdraw (W)')
    print('Balance (B)')

    while True:
        choice = input('Pick a letter: ').upper()

        if choice == 'T':
            bank = input('Choose bank to transfer: ')
            account = input('Input account number: ')
            name = input('Name of receiver: ')
            amount = input('Transfer amount: ')
            print(f'Transaction successful! Transferred {amount} to {name} at {bank}.')
        elif choice == 'D':
            amount = input('Amount to deposit: ')
            print(f'Transaction successful! Deposited {amount}.')
        elif choice == 'W':
            amount = input('Amount to withdraw: ')
            print(f'Transaction successful! Withdrew {amount}.')
        elif choice == 'B':
            balance = 10000  # assuming balance is 10,000 for example purposes
            print(f'Your balance is: {balance}')
        else:
            print('Incorrect input. Try again.')

ATM()
