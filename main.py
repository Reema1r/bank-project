import csv 

fields = ["account_id", "first_name", "last_name", "password","balance_checking","balance_savings" ]

rows = [ ["10001", "suresh", "sigera", "juagw362","1000","10000"],  
         ["10002", "james", "taylor", "idh36%@#FGd","10000","10000"],  
         ["10003", "melvin", "gordon", "uYWE732g4ga1","2000","20000"],  
         ["10004", "stacey", "abrams", "DEU8_qw3y72$","2000","20000"],  
         ["10005", "jake", "paul", "d^dg23g)@","100000","100000"]]

filename="bank.csv"

with open(filename, 'w') as csvfile:   
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)   
    csvwriter.writerows(rows) 


class BankCustomer():
    def __init__(self, account_id, first_name,last_name,password):
        self.account_id=account_id
        self.first_name=first_name
        self.last_name=last_name
        self.password=password




