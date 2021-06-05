# Random Walk problem in 2D, where each time, unit step can be taken at any of the four directions.
import random
import time

def random_walk(init_pos_x=0, init_pos_y=0, t_final=100):
    f = open("Random_Walk.dat", "w")
    x = init_pos_x
    y = init_pos_y
    t = [i for i in range(t_final + 1)]
    random_choice = [-1, 1]
    X = []; Y = []
    for _ in t:
        random_step = random.choice(random_choice)
        random_dimension = random.randint(0, 1)
        if random_dimension == 0:
            x += random_step
        else:
            y += random_step
        X.append(x)
        Y.append(y)
        f.write(f"{x}                                {y}    \n")
    f.close()
    return X, Y

random_walk(0, 0, 10000)
