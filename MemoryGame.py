import time
from random import randrange
from Utils import screen_cleaner

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        seq = []
        for i in range(1, self.difficulty):
            seq.append(randrange(1, 101))

        print(f"Remember the following sequins: {seq}")
        time.sleep(0.7)
        screen_cleaner()
        return seq

    def get_list_from_user(self):
        user_seq = []
        for i in range(1, self.difficulty):
            value = input(f"What is the number in position {i}: ")
            user_seq.append(int(value))

        return user_seq

    def is_list_equal(self, seq, user_seq):
        result = seq == user_seq
        if result:
            print("Congratulations! Your are correct!")
        else:
            print(f"Sorry, you lost. The correct sequence was: {seq}")

        return result

    def play(self):
        seq = self.generate_sequence()
        user_seq = self.get_list_from_user()

        return self.is_list_equal(seq, user_seq)