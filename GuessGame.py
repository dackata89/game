from random import randrange

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_number(self):
        return randrange(1, self.difficulty)

    def get_guess_from_user(self):
        user_number = input(f"Please provide value between 1 - {self.difficulty}\nValue: ")

        if int(user_number) not in range(1, self.difficulty):
            print(f"Uncorrected value, provided: {user_number}")
            user_number = self.get_guess_from_user()

        return user_number

    def compare_results(self, program, user):
        print(f"User provided value: {user}")
        print(f"Program value: {program}")
        return program == user

    def play(self):
        program_value = self.generate_number()
        user_value = self.get_guess_from_user()

        return self.compare_results(program_value, user_value)
