class Account:
    def __init__(self, balance):
        self.balance = balance

    def outgoing_transfer(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def incoming_transfer(self, amount):
        self.balance += amount


class PersonalAccount(Account):
    def __init__(self, first_name, last_name, balance, pesel):
        super().__init__(balance)
        self.first_name = first_name
        self.last_name = last_name
        if len(str(pesel)) != 11:
            self.pesel = "Invalid"
        else:
            self.pesel = pesel

    def express_outgoing_transfer(self, amount):
        fee = 1
        if self.balance >= amount:
            self.balance -= (amount + fee)


class CompanyAccount(Account):
    def __init__(self, company_name, balance, nip):
        super().__init__(balance)
        self.company_name = company_name
        if len(str(nip)) != 10:
            self.nip = "Invalid"
        else:
            self.nip = nip

    def express_outgoing_transfer(self, amount):
        fee = 5
        if self.balance >= amount:
            self.balance -= (amount + fee)