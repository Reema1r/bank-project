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
    fields = ["account_id", "first_name", "last_name", "password", "balance_checking", "balance_savings"]
    rows = [
        ["10001", "suresh", "sigera", "juagw362", "1000", "10000"],
        ["10002", "james", "taylor", "idh36%@#FGd", "10000", "10000"],
        ["10003", "melvin", "gordon", "uYWE732g4ga1", "2000", "20000"],
        ["10004", "stacey", "abrams", "DEU8_qw3y72$", "2000", "20000"],
        ["10005", "jake", "paul", "d^dg23g)@", "100000", "100000"]
    ]

    with open(bank_file, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)



class BankCustomer():
    def __init__(self, first_name,last_name,password, balance_checking =0 , balance_savings=0, overdraft_count=0,is_account_active= True):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.balance_checking=balance_checking
        self.balance_savings=balance_savings
        self.overdraft_count=overdraft_count
        self.is_account_active=is_account_active

    def add_new_customer(self):
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
                    return False
            
            if existing_ids:
                    new_customer_id=max(existing_ids)+1 # set the new_id to be the max id +1 
            
        except FileNotFoundError:
            print("Sorry,the file not found. Can't add a new customer")
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

# class Account():
#     def __init__(self, account_id, balance_checking,balance_savings):
#         self.account_id=account_id
#         self.balance_checking=balance_checking
#         self.balance_savings=balance_savings
        
#     def wihdraw_from_checking_account():
#         pass
        
#     def wihdraw_from_savings_account(): 
#         pass
    
    

    
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
        pass
    else:
        print("Invalid input")

