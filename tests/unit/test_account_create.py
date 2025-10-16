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