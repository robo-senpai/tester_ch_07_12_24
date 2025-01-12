import time
import pytest

def slow_function():
    """
    funkcja, ktora symuluje wolne dzialanie
    tutaj usypiamy program na 0.5s
    """

    time.sleep(0.5)
    return 'Done'

@pytest.mark.benchmark
def test_slow_function(benchmark):
    """
    funkcja, ktora przeprowadzi test sprawdzajacy, ile srednio zajmuje wykonanie slow function
    """
     
    result = benchmark(slow_function)
    assert result == 'Done'