import random

def create_random_list_of_integers(N: int, seed: int = None):
    if seed:
        random.seed(seed)
    random_list = list(range(1, N+1))
    random.shuffle(random_list)
    return random_list

if __name__ == "__main__":
    random_list = create_random_list_of_integers(59, seed=118) # For first imaging session with proper setup on 1/18/2025
    # [6, 42, 4, 5, 16, 17, 53, 43, 27, 8, 36, 13, 23, 30, 28, 40, 55, 31, 29, 35, 15, 54, 11, 57, 21, 18, 47, 49, 3, 26, 58, 52, 25, 9, 14, 1, 44, 38, 10, 34, 37, 48, 59, 33, 32, 39, 51, 22, 56, 2, 50, 19, 24, 45, 7, 20, 12, 41, 46]
    print(random_list)