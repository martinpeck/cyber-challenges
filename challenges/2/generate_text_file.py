from random import randint

with open('test.txt', mode='w') as t:
    for _ in range(500):
        for _ in range(80):
            t.write(str(randint(0,9)))

        t.write('\n')
