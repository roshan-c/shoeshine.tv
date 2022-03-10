from numpy import random
seed = random.randint(10000,99999)
print(seed)
seedsave = open("seed.txt", "a")
seedsave.write(str(seed))
seedsave.close()
print("Server seed succesfully generated")