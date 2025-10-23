from src.account import Account, CompanyAccount


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", 0.0, "12345678900")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0

    def test_pesel_too_log(self):
        account = Account("Jane", "Doe", 100.0, "12345678900123")
        assert account.pesel == "Invalid"

    def test_pesel_too_short(self):
        account = Account("Alice", "Smith", 50.0, "12345")
        assert account.pesel == "Invalid"

    def test_pesel_none(self):
        account = Account("Bob", "Brown", 75.0, None)
        assert account.pesel == "Invalid"

class TestAccountTransfer:
    def test_outgoing_transfer_success(self):
        account = Account("John", "Doe", 100.0, "12345678901")
        account.outgoing_transfer(50.0)
        assert account.balance == 50.0

    def test_outgoing_transfer_insufficient_funds(self):
        account = Account("Jane", "Doe", 30.0, "12345678902")
        account.outgoing_transfer(50.0)
        assert account.balance == 30.0

    def test_outgoing_transfer_exact_balance(self):
        account = Account("Alice", "Smith", 100.0, "12345678903")
        account.outgoing_transfer(100.0)
        assert account.balance == 0.0

    def test_incoming_transfer(self):
        account = Account("Bob", "Brown", 50.0, "12345678904")
        account.incoming_transfer(30.0)
        assert account.balance == 80.0

    def test_incoming_transfer_zero_balance(self):
        account = Account("Charlie", "White", 0.0, "12345678905")
        account.incoming_transfer(100.0)
        assert account.balance == 100.0

class TestCompanyAccount:
    def test_company_account_creation(self):
        account = CompanyAccount("Tech Solutions", 1000.0, "1234567890")
        assert account.company_name == "Tech Solutions"
        assert account.balance == 1000.0
        assert account.nip == "1234567890"

    def test_nip_too_long(self):
        account = CompanyAccount("Big Corp", 500.0, "12345678901234")
        assert account.nip == "Invalid"

    def test_nip_too_short(self):
        account = CompanyAccount("Small Biz", 200.0, "12345")
        assert account.nip == "Invalid"

    def test_nip_none(self):
        account = CompanyAccount("Mystery Inc", 300.0, None)
        assert account.nip == "Invalid"


class TestCompanyAccountTransfer:
    def test_outgoing_transfer_success(self):
        account = CompanyAccount("Tech Corp", 1000.0, "1234567890")
        account.outgoing_transfer(300.0)
        assert account.balance == 700.0

    def test_outgoing_transfer_insufficient_funds(self):
        account = CompanyAccount("Startup Ltd", 100.0, "9876543210")
        account.outgoing_transfer(200.0)
        assert account.balance == 100.0

    def test_outgoing_transfer_exact_balance(self):
        account = CompanyAccount("Final Corp", 500.0, "1111111111")
        account.outgoing_transfer(500.0)
        assert account.balance == 0.0

    def test_incoming_transfer(self):
        account = CompanyAccount("Rich Inc", 2000.0, "2222222222")
        account.incoming_transfer(500.0)
        assert account.balance == 2500.0

    def test_incoming_transfer_zero_balance(self):
        account = CompanyAccount("New Venture", 0.0, "3333333333")
        account.incoming_transfer(1000.0)
        assert account.balance == 1000.0
