class Account:
    def __init__(self, first_name, last_name, balance, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        if len(str(pesel)) != 11:
            self.pesel = "Invalid"
        else:
            self.pesel = pesel

    def outgoing_transfer(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def incoming_transfer(self, amount):
        self.balance += amount


class CompanyAccount:
    def __init__(self, company_name, balance, nip):
        self.company_name = company_name
        self.balance = balance
        if len(str(nip)) != 10:
            self.nip = "Invalid"
        else:
            self.nip = nip

    def outgoing_transfer(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def incoming_transfer(self, amount):
        self.balance += amount