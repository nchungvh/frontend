import random
import json
x = [{}]*3
for i in range(50):
    for k in range(3):
        x[k]['com' + str(i)] = ['ent' + str(random.randint(0,50)) for m in range(20)]
for i, j in enumerate(x):
    with open('test{}.json'.format(i), 'w') as f:
        json.dump(j, f)