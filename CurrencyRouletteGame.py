from random import randrange


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.exchange_rate = 3.72

    def get_money_interval(self, usd_amount):
        value_in_ils = usd_amount * self.exchange_rate
        margin = 5 - self.difficulty
        return value_in_ils - margin, value_in_ils + margin

    def get_guess_from_user(self, usd_amount):
        return float(input(f"Guess the value in ILS for {usd_amount} USD: "))

    def is_guess_correct(self, interval, user_guess):
        if interval[0] <= user_guess <= interval[1]:
            print("Congratulations! You won!")
            return True
        else:
            print(f"Sorry, you lost. The correct value was between {interval[0]:.2f} and {interval[1]:.2f}")
            return False

    def play(self):
        usd_amount = randrange(1, 100)
        interval = self.get_money_interval(usd_amount)
        user_guess = self.get_guess_from_user(usd_amount)

        return self.is_guess_correct(interval, user_guess)