import random

def generate(data):

    a = random.randint(1, 10)
    data["params"]["a"] = a

    Interval = 100/a 
    data["correct_answers"]["Interval"] = Interval

    return data
