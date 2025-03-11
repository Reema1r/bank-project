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
        ["10005", "jake", "paul", "d^dg23g)@", "100000", "100000",0,True]
    ]

    with open(bank_file, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)



class BankCustomer():
    def __init__(self,first_name,last_name,password, balance_checking =0 , balance_savings=0, overdraft_count=0,is_account_active= True):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.balance_checking=balance_checking
        self.balance_savings=balance_savings
        self.overdraft_count=overdraft_count
        self.is_account_active=is_account_active

    def check_customer_existence(self):
        existing_ids=[]
        existing_customers=[]
        new_customer_id=100001 #if the file empty, assign the id to 10001
        try:
            with open(bank_file , "r",newline="") as file:
                    csvfile=csv.reader(file)
                    next(csvfile) #to skip the header line
                    for lines in csvfile:
                        if lines: # check if there is lines
                            existing_ids.append(int(lines[0]))
                            existing_customers.append((lines[1], lines[2]))

            #Check if the customer already exist before adding it to the CSV file
            for first, last in existing_customers:
                first=first.lower().strip()
                last=last.lower().strip()
                
                if first == self.first_name.lower().strip() and last == self.last_name.lower().strip() :
                    print("The customer you are trying to add is already exists")
                    return False , None
            
            if existing_ids:
                    new_customer_id=max(existing_ids)+1 # set the new_id to be the max id +1 
            
        except FileNotFoundError:
            print("Sorry,the file not found. Can't add a new customer")
            return False , None
        
        return True, new_customer_id

    def add_new_customer(self):
        exists, new_customer_id = self.check_customer_existence()
        if not exists:  # if exists = False , then not exists = True >> customer exists (can't add)
                        # if exists = True , then not exists = False >> customer doesn't exists (can add)
            return False
        
        new_customer_info = [new_customer_id, 
                            self.first_name,
                            self.last_name,
                            self.password,
                            self.balance_checking,
                            self.balance_savings]

        with open(bank_file, "a", newline="") as csvfile: 
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(new_customer_info) # add the new customer info to the CSV file
            print(f"The new customer [{self.first_name} {self.last_name}] has been added successfully")
        return True
    


class Account():
    def __init__(self, account_id, password, balance_checking=0,balance_savings=0,overdraft_count=0,is_account_active= True):
        self.account_id=account_id
        self.password=password
        self.balance_checking=balance_checking
        self.balance_savings=balance_savings
        self.overdraft_count=overdraft_count
        self.is_account_active= is_account_active
        
    def login(self):
        with open(bank_file , "r",newline="") as file:
                    csvfile=csv.reader(file)
                    next(csvfile) 
                    for lines in csvfile: 
                        if lines: 
                            account_id = lines[0].strip() #retrieves the id (colomn 1)
                            password = lines[3].strip() #retrieves the password (colomn 4)
                            
                            #check if the retrieved id and password matches the id and password entered
                            if account_id == self.account_id and password == self.password:
                                print(f"\nWelcome!,{lines[1]} {lines[2]}")
                                return True
                            
                    print("Invalid login attempt. Please check your details and try again")
                    return False
        
    def withdraw_options(self):
        account_choice=int(input("Which account you want to withdraw from? \n(1) Checking account \n(2) Savings account\n"))
        if account_choice == 1:
            withdraw_amount= float(input("Enter amount to withdraw from checking account: "))
            self.perform_withdraw(withdraw_amount, "checking")
            
        elif account_choice == 2:
            withdraw_amount= float(input("Enter amount to withdraw from savings account: "))
            self.perform_withdraw(withdraw_amount,"savings")
        else:
            print("Invalid choice. Please choose 1 or 2")
            
            
    def perform_withdraw(self, withdraw_amount, account_type):
        #check if the user is active
        if not self.is_account_active:
            print("Account is deactivated due to excessive overdrafts")
            return False
        
        #check if the input amount is valid 
        if withdraw_amount <= 0:
            print("Withdraw amount must be positive value")
            return False
        
        #assign the current balance to be the balance of the account_type entred
        if account_type =="checking":
            current_balance = self.balance_checking
        else:
            current_balance = self.balance_savings
            
            
        if current_balance<0:
            if withdraw_amount >100:
                print("Your account is negative, you can not withdraw more than 100$")
                return False
            if (current_balance - withdraw_amount) < -100:
                print("Your withdrawal would result in an account balance less than 100$")
                return False
            self.overdraft_count +=1
            
            if self.overdraft_count >=2:
                self.is_account_active = False
            
        if withdraw_amount > current_balance:
            print("Sorry. The amount you are trying to withdraw is greater than your account balance")
            return False
        
        if account_type == "checking":
            self.balance_checking-=withdraw_amount
            print(f"New checking account balance after withdrawal: {self.balance_checking}")
        else:
            self.balance_savings-=withdraw_amount
            print(f"New savings account balance after withdrawal: {self.balance_savings}")
            
        # self.update_csv(account_type)
        return True
    
    def perform_deposit(self, deposit_amount, account_type):
        #check if the input amount is valid 
        if deposit_amount <= 0:
            print("Deposit amount must be positive value")
            return False
        
        if account_type == "checking":
            self.balance_checking+=deposit_amount
            print(f"New checking account balance after deposit: {self.balance_checking}")
        else:
            self.balance_savings+=deposit_amount
            print(f"New savings account balance after deposit: {self.balance_savings}")
            
        # self.update_csv(account_type)
        return True



if __name__== "__main__":
    print("********** Welcome to ACME Bank **********")
    start_option=int(input("What do you want to do? \n(1) Add new customer \n(2) Log in \n"))

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
            existing_customer.withdraw_options()
    else:
        print("Invalid input")

