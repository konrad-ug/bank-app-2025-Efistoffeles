from src.account import Account


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
