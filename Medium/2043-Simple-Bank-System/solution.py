class Bank:

    def __init__(self, balance: List[int]):
        self.balance = {}
        for i in range(len(balance)):
            self.balance[i+1] = balance[i]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > len(self.balance.keys()):
            return False
        if account2 < 1 or account2 > len(self.balance.keys()):
            return False
        if money > self.balance[account1]:
            return False
        self.balance[account1]-=money
        self.balance[account2]+=money
        return True
        
    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > len(self.balance.keys()):
            return False
        self.balance[account]+=money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > len(self.balance.keys()) or money > self.balance[account]:
            return False
        self.balance[account]-=money
        return True
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)