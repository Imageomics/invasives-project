import random

def create_random_list_of_integers(N: int, seed: int = None):
    if seed:
        random.seed(seed)
    random_list = list(range(1, N+1))
    random.shuffle(random_list)
    return random_list