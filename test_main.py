import unittest
from main import BankCustomer 
from main import Account


class TestBankCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 =BankCustomer("Reema","Radi","pass1234",0,0) 
        self.customer2 =BankCustomer("reema","Radi","r01222",0,0) 
        self.customer3 =BankCustomer("Shouq","Radi","Sh@@ouq1",0,0) 
        self.customer4 = BankCustomer("rafeef","radi","pass12345@",0,0)
                
    def test_add_new_customer(self): 
        self.assertEqual(self.customer1.add_new_customer(), False) # if customer aleady exists
        self.assertEqual(self.customer2.add_new_customer(), False) # if the customer already exists (case insensitive)
        self.assertEqual(self.customer3.add_new_customer(), True) # if the customer doesn't exists
    
    def test_check_customer_existence(self):
        exists, _ = self.customer1.check_customer_existence() #customer exists
        self.assertFalse(exists)
        
        exists, _ =self.customer4.check_customer_existence() # customer does not exists
        self.assertEqual(exists,True)


class TestWithdraw(unittest.TestCase):    
    def setUp(self):
        self.customer5 =Account("10009","pass1234") 
        self.customer5.balance_checking=1500
        self.customer5.balance_savings=-30
        
    def test_withdraw_from_account(self):
        self.assertEqual(self.customer5.perform_withdraw(-30,"checking"), False) # unsuccessful withdraw (negative withdraw amount)
        self.assertEqual(self.customer5.perform_withdraw(0, "savings"), False) # unsuccessful withdraw (zero withdraw amount)

        # Test if the account balance > 0
        self.assertEqual(self.customer5.perform_withdraw(500,"checking"), True) # successful withdraw
        self.assertEqual(self.customer5.perform_withdraw(4000,"checking"), False) # unsuccessful withdraw (insufficient account balance)
        
        # Test if the account balance <0
        self.assertEqual(self.customer5.perform_withdraw(20, "savings"), True) # successful withdraw (negative balance, withdraw amount < 100$ , resulting balance > -$100)
        self.assertEqual(self.customer5.perform_withdraw(150,"savings"), False) # unsuccessful withdraw (negative balance and trying to withdraw more than 100$)
        self.assertEqual(self.customer5.perform_withdraw(80, "savings"), False) # unsuccessful withdraw (negative balance, withdraw amount < 100$ , resulting balance < -$100 )
        
        
        
class TestDeposit(unittest.TestCase):  
    def setUp(self):
        self.customer6 =Account("10010","pass1234@") 
        self.customer6.balance_checking=100
        self.customer6.balance_savings=800
        
    def test_deposit_to_account(self):
        self.assertEqual(self.customer6.perform_deposit(200,"checking"), 300) # successful deposit
        self.assertEqual(self.customer6.perform_deposit(-200,"checking"), False) # unsuccessful deposit (negative deposit amount)
        self.assertEqual(self.customer6.perform_deposit(0 ,"savings" ), False) # unsuccessful deposit (zero deposit amount)
        
        

if __name__== "__main__":
    unittest.main(verbosity=2)