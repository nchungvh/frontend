import json
import random
knn = {'com_{}'.format(i): 'https://www.youtube.com/watch?v=Soa3gO7tL-c' for i in range(51)}
cate = {'com_{}'.format(i): ['cate_{}'.format(random.randint(0,10)) for j in range(2)] for i in range(50)}
print(knn)
with open('url_test.json','w', encoding = 'utf-8') as f:
    json.dump(knn, f)

# with open('cate_test.json','w', encoding = 'utf-8') as f:
#     json.dump(cate, f)   