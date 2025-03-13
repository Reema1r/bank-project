#Resources Used:
# Check if a CSV file already exists: https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
# Create CSV file:https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/
# Append new customer to the existing CSV file (BankCustomer class - add_new_customer() method):https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/
# Skip the header line: https://www.quora.com/How-do-you-skip-a-line-when-reading-a-file-in-Python


import csv 
import os

bank_file="bank.csv"

# Check if the CSV exists before creating a new one to ensure that existing data is not erased
# If doesn't exist, then create a new CSV file with the following predifined info
if not os.path.isfile(bank_file):
    fields = ["account_id", "first_name", "last_name", "password", "balance_checking", "balance_savings","overdraft_count","is_account_active"]
    rows = [
        ["10001", "suresh", "sigera", "juagw362", "1000", "10000",0,True],
        ["10002", "james", "taylor", "idh36%@#FGd", "10000", "10000",0,True],
        ["10003", "melvin", "gordon", "uYWE732g4ga1", "2000", "20000",0,True],
        ["10004", "stacey", "abrams", "DEU8_qw3y72$", "2000", "20000",0,True],
        ["10005", "jake", "paul", "d^dg23g)@", "100000", "100000",0,True],
        ["10006", "reema", "radi", "pass1234", "1000", "10000",0,True]
    ]

    with open(bank_file, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)



class BankCustomer():
    """
    This class represents a customer in the bank system. Handles customer creation and checks for duplicates
    """
    
    """
    Initializes a new customer object with the given personal and account details
    """
    def __init__(self,first_name,last_name,password, balance_checking =0 , balance_savings=0, overdraft_count=0,is_account_active= True):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.balance_checking=balance_checking
        self.balance_savings=balance_savings
        self.overdraft_count=overdraft_count
        self.is_account_active=is_account_active

    
    def check_customer_existence(self):
        """
        This method checks if the customer already exists in the CSV file by matching their first and last name
        Returns: A tuple (boolean,ID), first element indicates wheather the customer exists or not, the second element is either new ID or None
        """
        existing_ids=[] # To store existing customer IDs retrieved from CSV
        existing_customers=[] # To store existing customers names (first, last)
        new_customer_id=100001 # Assign the ID to 10001, if the file is empty
        
        try:
            with open(bank_file , "r",newline="") as file:
                    csvfile=csv.reader(file)
                    next(csvfile) # To skip the header line
                    for lines in csvfile:
                        if lines: # To check if there is a line to proccess
                            existing_ids.append(int(lines[0]))
                            existing_customers.append((lines[1], lines[2]))

            #Check if the customer already exist before adding it to the CSV by comparing names
            for first, last in existing_customers:
                first=first.lower().strip()
                last=last.lower().strip()
                
                if first == self.first_name.lower().strip() and last == self.last_name.lower().strip() :
                    print("The customer you are trying to add already exists")
                    return False , None # Return (False, None) if the customer exists
            
            # If the list of existing IDs is not empty, assign the new customer ID to be one higher than the max ID
            if existing_ids:
                    new_customer_id=max(existing_ids)+1 # Set the new ID to be the max ID +1 
            
        except FileNotFoundError:
            print("Sorry,the file not found. Can't add a new customer")
            return False , None
        
        return True, new_customer_id # Return (True, new customer ID) if customer does not exists


    def add_new_customer(self):
        """
        This method adds a new customer to the CSV file if the customer does not already exists
        Returns: A bool value of True if the new customer was added successfully, False otherwise
        """
        if not self.first_name or not self.last_name:
            print("Name cannot be empty. Please enter a valid name")
            return False
        elif self.first_name.isdigit() or self.last_name.isdigit():
            print("Name cannot be a number. Please enter a valid name")
            return False
        elif not self.password:
            print("Password cannot be empty. Please enter a valid password")
            return False
            
        exists, new_customer_id = self.check_customer_existence() # Check if the customer exists
        if not exists:  # if exists = False , then not exists = True >> customer exists (can't add)
                        # if exists = True , then not exists = False >> customer doesn't exists (can add)
            return False
        
        new_customer_info = [new_customer_id, 
                            self.first_name,
                            self.last_name,
                            self.password,
                            self.balance_checking,
                            self.balance_savings,
                            self.overdraft_count,
                            self.is_account_active
                            ]
        # Open the CSV file in append mode and add the new customer info
        with open(bank_file, "a", newline="") as csvfile: 
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(new_customer_info) # Add the new customer info to the CSV file
            print(f"The new customer [{self.first_name} {self.last_name}] has been added successfully")
        return True 
    

# ****************************************************************************************************************
class Account():
    """
    This class represents a bank account. It manage account login, logout, and handles 
    the user account information such as balance
    """
    
    """
    Initializes a new account object with the given details
    """
    def __init__(self, account_id, password, balance_checking=0,balance_savings=0,overdraft_count=0,is_account_active= True):
        self.account_id=account_id
        self.password=password
        self.balance_checking=balance_checking
        self.balance_savings=balance_savings
        self.overdraft_count=overdraft_count
        self.is_account_active= is_account_active
        
    def login(self):
        """
        This method reads the CSV file containing account details, checks if the entered 
        account ID and password match any existing account, and if so, retrieve the account details
        (checking balance, savings balance, overdraft count, account status). 

        Returns: A boolean value of True if login is successful, False otherwise
        """
        with open(bank_file , "r",newline="") as file:
            csvfile=csv.reader(file)
            next(csvfile) 
            for lines in csvfile: 
                if lines: 
                    account_id = lines[0].strip() #retrieves the ID (colomn 1)
                    password = lines[3].strip() #retrieves the password (colomn 4)
                            
                    # Check if the retrieved id and password matches the id and password entered, then load account details if the login is successful
                    if account_id == self.account_id and password == self.password:
                        self.balance_checking = float(lines[4].strip())  
                        self.balance_savings = float(lines[5].strip())  
                        self.overdraft_count = int(lines[6].strip())  
                        self.is_account_active = lines[7].strip().lower() == 'true'
                        
                        print(f"\nWelcome!,{lines[1]} {lines[2]}")
                        return True
                            
            print("Invalid login attempt. Please check your details and try again")
            return False
        
    def logout(self):
        print("You have logged out successfuly")
        return False
                
    def transaction_option(self):
        """
        This method asks the user to select a transaction option to perform the corresponding transaction,
        if the entered option is invalid option, the user is will be asked again for a valid input
        """
        while True:
            option = int(input("\nWhat would you like to do? \n(1) Withdraw \n(2) Deposit \n(3) Transfer Money \n(4) Logout\n"))
                    
            if option == 1:
                existing_customer.withdraw_options()
            elif option == 2:
                existing_customer.deposit_options()
            elif option == 3:
                self.transfer_money()
            elif option == 4:
                return self.logout()
            else:
                print("Invalid input. Please choose a valid option.")
                
                
    def update_csv(self):
        """
        This method updates the bank CSV file and ensures that the CSV file always has the latest info for the account after a transaction
        It will read the CSV file and looks for the account matching the current account ID
        If match found, if will update the info and writes the updated account info back into the CSV file
        """
        lines=[]
        with open(bank_file , "r",newline="") as file:
            csvreader=csv.reader(file)
            headers = next(csvreader) # retrieve the first line of the CSV file (header line)
            for line in csvreader:
                if line and line[0] == self.account_id:
                    line[4]=self.balance_checking
                    line[5]=self.balance_savings
                    line[6]=self.overdraft_count
                    line[7]=self.is_account_active
                lines.append(line)
                
        with open(bank_file , "w", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(headers) 
            csvwriter.writerows(lines)
            
# ****************************************************************
    def withdraw_options(self):
        """
        This method asks the user to choose which account to withdraw from (checking or savings)
        Depending on the user choice, it requests the withdrawal amount and calls 
        `perform_withdraw` method to perform the withdraw
        """
        
        account_choice=int(input("Which account you want to withdraw from? \n(1) Checking account \n(2) Savings account\n"))
        
        if account_choice == 1:
            withdraw_amount= input("Enter amount to withdraw from checking account: ")
            self.perform_withdraw(withdraw_amount, "checking")
            
        elif account_choice == 2:
            withdraw_amount= input("Enter amount to withdraw from savings account: ")
            self.perform_withdraw(withdraw_amount,"savings")
        else:
            print("Invalid choice. Please choose 1 or 2")
            
    
    def perform_withdraw(self, withdraw_amount, account_type):
        """
        This method processes the withdrawal for the given account type (checking or savings)
        It checks and ensures that the withdrawal amount is valid and the account balance will not go below -100 
        It also updates the account balances, applies overdraft fees, and deactivates the account after 2 overdrafts
        """
        
        try:
            if withdraw_amount == "":
                raise ValueError("Withdrawal amount cannot be empty")
            
            withdraw_amount = float(withdraw_amount)  
        
            if withdraw_amount <= 0:
                raise ValueError("Withdrawal amount must be a positive number")
                
        except ValueError as error:
            print(f"Invalid input. {error}")
            return False 
        
        # Check if the account has been deactivated
        if self.overdraft_count == 2:
            print("acoount is deactivated due to excessive overdrafts")
            self.logout()
            return False
        
        # Set the current balance based on the account type
        if account_type =="checking":
            current_balance = self.balance_checking
        else:
            current_balance = self.balance_savings
            
        
        # Check if the withdrawal can be made without going below -100
        if (current_balance - withdraw_amount) < -100:
            print("Cannot withdraw, balance will exceed overdraft limit")
            return False
        
        # If the current balance is non negative
        if current_balance >= 0:
            if account_type == "checking":
                self.balance_checking -= withdraw_amount
                print(f"New checking account balance after withdrawal: {self.balance_checking}")
                # Check if the checking balance became less than zero, then apply overdraft fee
                if self.balance_checking<0:
                    self.overdraft_count+=1
                    self.balance_checking-=35
                    
            else:
                self.balance_savings -= withdraw_amount
                print(f"New savings account balance after withdrawal: {self.balance_savings}")
                # Check if the savings balance became less than zero, then apply overdraft fee
                if self.balance_savings<0:
                    self.overdraft_count+=1
                    self.balance_savings-=35
        
        # If the current balance is negative
        else:
            if account_type == "checking":
                self.balance_checking -= withdraw_amount
                self.balance_checking-=35
                print(f"New checking account balance after withdrawal: {self.balance_checking}")
            else:
                self.balance_savings -= withdraw_amount
                self.balance_checking-=35
                print(f"New savings account balance after withdrawal: {self.balance_savings}")

            
            self.overdraft_count += 1
            # Check if the overdraft count reaches 2, if so, deactivate the account
            if self.overdraft_count >= 2:
                self.is_account_active = False
                print("Account deactivated due to excessive overdrafts.")
                self.update_csv()
                
        self.update_csv()
        return True
    
    def deposit_options(self):
        """
        This method asks the user to choose which account to deposit to (checking or savings)
        Depending on the user choice, it requests the deposit amount and calls 
        `perform_deposit` method to perform the deposit
        """
        account_choice=int(input("Which account you want to deposit to? \n(1) Checking account \n(2) Savings account\n"))
        
        if account_choice == 1:
            deposit_amount= input("Enter amount to deposit to checking account: ")
            self.perform_deposit(deposit_amount, "checking")
            
        elif account_choice == 2:
            deposit_amount= input("Enter amount to deposit to savings account: ")
            self.perform_deposit(deposit_amount,"savings")
        else:
            print("Invalid choice. Please choose 1 or 2")
            
            

    def perform_deposit(self, deposit_amount, account_type):
        """
        This method processes the deposit for the given account type (checking or savings)
        It checks and ensures that the deposit amount is valid, then updates the account balances and save changes to the CSV file
        """
        
        try:
            if deposit_amount =="":
                raise ValueError("Deposit amount cannot be empty")
                
            deposit_amount=float(deposit_amount)
                
            if deposit_amount <= 0:
                raise ValueError("Deposit amount must be a positive number")
                
        except ValueError as error:
                print(f"Invalid input. {error}")
                return False
            
        if account_type == "checking":
            self.balance_checking += deposit_amount
            print(f"New checking account balance after deposit: {self.balance_checking}")
        else:
            self.balance_savings += deposit_amount
            print(f"New savings account balance after deposit: {self.balance_savings}")
            
        self.update_csv()
        return True


    def get_recipient_account(self, recipient_account_id):
        """
        This method retrieve the recipient account by seaching for their account ID in the bank file
        Return: Account object if found, otherwise None
        """
        # Try to find the recipient account from the bank file
        with open(bank_file, "r", newline="") as file:
            csvfile = csv.reader(file)
            next(csvfile)  
            for lines in csvfile:
                if lines and lines[0] == recipient_account_id:
                    # Returning recipient account details 
                    recipient_account = Account(lines[0], lines[3], float(lines[4]), float(lines[5]), int(lines[6]), lines[7].lower() == 'true')
                    return recipient_account
        return None  

    def transfer_money(self):
        """
        This method handles transfers transactions including (checking to savings, savings to checking or to another customer account)
        It asks the user which account to transfer from, the transfer amount, and the recipient account ID. 
        """
        transfer_option = int(input("Which account do you want to transfer from? \n(1) Checking to Savings \n(2) Savings to Checking \n(3) To another customer account\n"))
        
        
        if transfer_option == 1:
            transferred_amount = float(input("Enter amount to transfer from checking to savings: "))
            
            # Ensure that the transfer amount is positive
            if transferred_amount <=0:
                print("Transfer amout must be positive value")
                return False
            
            # Check if account balance is sufficient 
            if transferred_amount >self.balance_checking:
                print("Can not transfer due to insufficient balance in checking account")
                return False
            
            # Update account balances after transfer
            self.balance_checking-=transferred_amount
            self.balance_savings+=transferred_amount
            print(f"Transferred {transferred_amount} from checking to savings")
            self.update_csv()
            
            
        elif transfer_option == 2:
            transferred_amount = float(input("Enter amount to transfer from savings to checking: "))
            
            # Ensure that the transfer amount is positive
            if transferred_amount <=0:
                print("Transfer amout must be positive value")
                return False
            
            # Check if account balance is sufficient 
            if transferred_amount > self.balance_savings:
                print("Can not transfer due to insufficient balance in savings account")
                return False
            
            # Update account balances after transfer
            self.balance_checking+=transferred_amount
            self.balance_savings-=transferred_amount
            print(f"Transferred {transferred_amount} from savings to checking {self.balance_savings}")
            self.update_csv()
            
            
        elif transfer_option ==3:
            recipient_account_id = input("Enter the recipient account ID: ")
            account_to_transfer_from=int(input("Which account do you want to transfer from? \n(1) Checking \n(2) Savings\n"))
            transferred_amount = float(input("Enter amount to transfer to another customer account: "))
            
            # Ensure that the transfer amount is positive
            if transferred_amount <=0:
                print("Transfer amout must be positive value")
                return False
            
            # Retrieve the recipient account 
            recipient_account = self.get_recipient_account(recipient_account_id)
            if not recipient_account: # Not found
                print("Recipient account not found")
                return False
            
            
            # Manages transfer from checking account
            if account_to_transfer_from == 1:
                if transferred_amount > self.balance_checking:
                    print("Can not transfer due to insufficient balance in checking account")
                    return
                self.balance_checking -= transferred_amount
                recipient_account.balance_checking += transferred_amount  
                print(f"Transferred {transferred_amount} from your checking to recipient checking account")
        
            # Manages transfer from savings account
            elif account_to_transfer_from == 2:
                if transferred_amount > self.balance_savings:
                    print("Can not transfer due to insufficient balance in checking account")
                    return
                self.balance_savings -= transferred_amount
                recipient_account.balance_savings += transferred_amount  
                print(f"Transferred {transferred_amount} from your savings to recipient checking account")
            self.update_csv()
            recipient_account.update_csv()
            
        
        else:
            print("Invalid transfer option. Please choose a valid option")
            return False

if __name__== "__main__":
    print("********** Welcome to ACME Bank **********")
    start_option=int(input("Welcome to our bank. Please select one of the following options:\n"
                        "(1) Add new customer\n"
                        "(2) Log in \n"
                        "Your choice:"))

    if start_option == 1:
        first_name =input("Enter first name: ")
        last_name =input("Enter last name: ")
        password =input("Enter password: ")
        new_customer= BankCustomer(first_name,last_name, password) #create a new object of BankCustomer class
        new_customer.add_new_customer()
    
    elif start_option == 2:
        account_id =input("Enter account id: ")
        password =input("Enter password: ")
        existing_customer = Account(account_id, password)  
        if existing_customer.login():
            existing_customer.transaction_option()
    else:
        print("Invalid input")