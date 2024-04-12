import random

class ListeCreator :
    def create_random_array(length):
        return [random.randint(1, 10000000000) for _ in range(length)]