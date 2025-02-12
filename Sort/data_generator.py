import random
from Sort import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    return [random.randint(0, limit) for _ in range(size)]
