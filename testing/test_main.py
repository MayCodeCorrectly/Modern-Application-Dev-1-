from main import is_prime

def test_is_prime():
    assert is_prime(10) == False
    assert is_prime(2) == True

# to run open terminal and do "pytest test_main.py"