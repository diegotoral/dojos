# -*- coding: utf-8 -*-


class FizzBuzz():
    def get(self):
        return [self._process(n) for n in range(1, 101)]

    def is_fizz(self, number):
        return number % 3 == 0

    def is_buzz(self, number):
        return number % 5 == 0

    def is_fizz_buzz(self, number):
        return self.is_fizz(number) and self.is_buzz(number)

    def _process(self, number):
        if self.is_fizz(number):
            return 'Fizz'
        elif self.is_buzz(number):
            return 'Buzz'
        elif self.is_fizz_buzz(number):
            return 'Fizz Buzz'
        else:
            return number
