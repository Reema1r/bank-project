# create CSV file:https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/
# append new customer to the existing CSV file (BankCustomer class - add_new_customer() method):https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/
import csv 

# create a new CSV file
fields = ["account_id", "first_name", "last_name", "password","balance_checking","balance_savings" ]
rows = [ ["10001", "suresh", "sigera", "juagw362","1000","10000"],  
        ["10002", "james", "taylor", "idh36%@#FGd","10000","10000"],  
        ["10003", "melvin", "gordon", "uYWE732g4ga1","2000","20000"],  
        ["10004", "stacey", "abrams", "DEU8_qw3y72$","2000","20000"],  
        ["10005", "jake", "paul", "d^dg23g)@","100000","100000"]]

bank_file="bank.csv"
with open(bank_file, 'w') as csvfile:   
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)   
    csvwriter.writerows(rows) 


class BankCustomer():
    def __init__(self, account_id, first_name,last_name,password):
        self.account_id=account_id
        self.first_name=first_name
        self.last_name=last_name
        self.password=password

    def add_new_customer(self, balance_checking =0 , balance_savings=0, bank_file="bank.csv"):
        new_customer_info = [self.account_id, 
                            self.first_name,
                            self.last_name,
                            self.password,
                            balance_checking,
                            balance_savings]

        with open(bank_file, 'a') as csvfile: 
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(new_customer_info) # add (write) the new customer info to the CSV file


customer = BankCustomer("10006", "Reema", "Radi", "pass1234") #create a new object of BankCustomer class
customer.add_new_customer()  #call add_new_customer() to add it to the CSV file


# class Account():
#     def __init__(self, account_id, balance_checking,balance_savings):
#         self.account_id=account_id
#         self.balance_checking=balance_checking
#         self.balance_savings=balance_savings



