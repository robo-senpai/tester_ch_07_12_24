from kod import fizzbuzz


def test_number():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
def test_fizz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(6) == 'Fizz'
    assert fizzbuzz(9) == 'Fizz'


def test_buzz():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(20) == 'Buzz'


def test_fizzbuzz():
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(30) == 'FizzBuzz'
    assert fizzbuzz(450) == 'FizzBuzz'


def test_fizzbuzz_negative():
    assert fizzbuzz(-3) == None


def test_fizzbuzz_string():
    assert fizzbuzz('Mama') == None


def test_fizzbuzz_float():
    assert fizzbuzz(5.7) == 'Buzz'