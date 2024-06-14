class Account:
  def __init__(self,bal,acc) -> None:
    self.balance=bal
    self.account_no=acc
  #debit Method
  def debit(self,amount):
    self.balance -= amount
    print("Rs." , amount,"was debited from your ac:/",self.account_no)
    print("total balance =",self.get_balance())
    
    
  #Credit Method
  def credit(self,amount):
    self.balance +=amount
    print("Rs." , amount,"was Credited to your ac:/",self.account_no)
    print("total balance =",self.get_balance())
    
  def get_balance(self):
    return self.balance  

acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(5000)

    