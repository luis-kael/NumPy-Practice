import numpy as np 

rng = np.random.default_rng(seed=1)

array = np.array([1, 2, 3, 4, 5])

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])

fruits = rng.choice(fruits, size= (3, 3))

print(rng.integers(low = 1, high = 101, size = (3, 2)))

print(np.random.uniform(low = -1, high= 1, size = (3, 2))) # Float

print(rng.shuffle(array))

print(fruits)