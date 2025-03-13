import unittest
from main import BankCustomer 
from main import Account


class TestAddBankCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = BankCustomer("Ghada","Almutairi","GH@@1")
        self.customer2 = BankCustomer("reema","radi","pass1234") 
        self.customer3 = BankCustomer("REEMA","RADI","pass1234") 
        self.customer4 = BankCustomer("","","")
        self.customer5 = BankCustomer("10","20","rmrm22")
                
    def test_add_new_customer(self): 
        self.assertEqual(self.customer1.add_new_customer(), True) # if the customer doesn't exists
        self.assertEqual(self.customer2.add_new_customer(), False) # if customer aleady exists
        self.assertEqual(self.customer3.add_new_customer(), False) # if the customer already exists (case insensitive)
        self.assertEqual(self.customer4.add_new_customer(), False) # if inputs are empty 
        self.assertEqual(self.customer5.add_new_customer(), False) # if first and last names are numbers
        


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.account1 =Account("10001","pass1234")
        self.account2 =Account("10009","yjwndu")
        
    def test_login(self):
        self.assertEqual(self.account1.login(), True) # successful login
        self.assertEqual(self.account2.login(), False) # unsuccessful login
    
    
    
class TestWithdraw(unittest.TestCase):    
    def setUp(self):
        self.account3 =Account("10006","pass1234") 
        self.account4 =Account("10001","juagw362") 
        self.account5 =Account("10004","DEU8_qw3y72$") 
        
    def test_withdraw_from_account(self):
        self.assertEqual(self.account3.perform_withdraw(-30,"checking"), False) # unsuccessful withdraw (negative withdraw amount)
        self.assertEqual(self.account3.perform_withdraw(0, "savings"), False) # unsuccessful withdraw (zero withdraw amount)

        # Test if the account balance > 0
        self.assertEqual(self.account4.perform_withdraw(500,"checking"), True) # successful withdraw
        self.assertEqual(self.account4.perform_withdraw(4000,"checking"), False) # unsuccessful withdraw (insufficient account balance)
        
        # Test if the account balance <0
        self.assertEqual(self.customer5.perform_withdraw(20, "savings"), True) # successful withdraw (negative balance, withdraw amount < 100$ , resulting balance > -$100)
        self.assertEqual(self.customer5.perform_withdraw(150,"savings"), False) # unsuccessful withdraw (negative balance and trying to withdraw more than 100$)
        self.assertEqual(self.customer5.perform_withdraw(80, "savings"), False) # unsuccessful withdraw (negative balance, withdraw amount < 100$ , resulting balance < -$100 )
        
        

class TestDeposit(unittest.TestCase):  
    def setUp(self):
        self.account6 =Account("10002",10000,10000,0,True)
        
    def test_deposit_to_account(self):
        self.assertEqual(self.account6.perform_deposit(150,"checking"), True) # successful deposit
        self.assertEqual(self.account6.perform_deposit("Reema","checking"), False) # unsuccessful deposit
        self.assertEqual(self.account6.perform_deposit(-20,"savings"), False) # unsuccessful deposit
        self.assertEqual(self.account6.perform_deposit(0,"checking"), False) # unsuccessful deposit




# class TestTransferMoney(unittest.TestCase):  


if __name__== "__main__":
    unittest.main(verbosity=2)