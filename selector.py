import random

while True :
    num_of_sets = int(input("몇개살끼고"))
    if num_of_sets <= 0:
        print("몇번")
    else:
        for i in range(num_of_sets):
            numbers = random.sample(range(1,46),6)
            print(f"번호{i+1} : {sorted(numbers)}")
        break
