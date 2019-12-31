import pytest

from account import Account


@pytest.fixture(scope="session")
def basic_account():
    owner = "PyBob"
    return Account(owner)


@pytest.fixture(scope="session")
def account_01():
    owner = "PyBob"
    acc = Account(owner, 5)
    acc.add_transaction(5)
    acc.add_transaction(10)
    return acc


@pytest.fixture(scope="session")
def account_02():
    owner = "Julian"
    acc = Account(owner)
    acc.add_transaction(10)
    acc.add_transaction(-5)
    return acc


@pytest.fixture(scope="session")
def account_03():
    owner = "David"
    acc = Account(owner, 5)
    acc.add_transaction(15)
    return acc


def test_basic_account_class(basic_account):
    assert str(basic_account) == "Account of PyBob with starting amount: 0"
    assert repr(basic_account) == "Account('PyBob', 0)"
    assert basic_account.balance == 0
    assert len(basic_account) == 0


def test_basic_account_class_actions(basic_account):
    basic_account.add_transaction(5)
    assert basic_account.balance == 5
    assert len(basic_account) == 1
    assert basic_account.__getitem__(0) == 5
    basic_account.add_transaction(-15)
    assert basic_account.balance == -10
    assert len(basic_account) == 2


def test_account_class_incorrectly():
    with pytest.raises(TypeError):
        Account()


def test_account_class_invalid_transaction(basic_account):
    with pytest.raises(ValueError) as e:
        basic_account.add_transaction("a")
    assert str(e.value) == "please use int for amount"


def test_advanced_account_functions(account_01, account_02, account_03):
    assert account_02 < account_01
    assert account_01 > account_02
    assert not account_01 < account_01

    new_account = account_01 + account_02
    assert str(new_account) == "Account of PyBob&Julian with starting amount: 5"
    assert repr(new_account) == "Account('PyBob&Julian', 5)"
    assert new_account.balance == 25
    assert len(new_account) == 4
    assert (
        str(account_02 + account_01)
        == "Account of Julian&PyBob with starting amount: 5"
    )
