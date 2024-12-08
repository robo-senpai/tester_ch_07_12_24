# funkcja zastepujaca liczby podzielne przez 3 slowem Fizz
# a przez 5 slowem Buzz
def fizzbuzz(i):
    if isinstance(i, (int, float)) and i > 0:
        i = int(i)
        if i % 15 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0:
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'
        return i
    else:
        return None