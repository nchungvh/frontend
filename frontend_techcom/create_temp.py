com_dict = {}
cate_dict = {}
url_dict = {}
import random
for i in range(50):
    com_dict['com' + str(i)] = ['com' + str(random.randint(0,49)) for j in range(40)]
    cate_dict['com' + str(i)] = ['cate' + str(random.randint(0,10)) for j in range(5)]
    url_dict['com' + str(i)] = 'url' + str(i) 
temp = {'url': url_dict, 'cate': cate_dict}
import json
with open('test_top40.json' ,'w') as f:
    json.dump(com_dict, f)

with open('test_url_cate.json' ,'w') as f:
    json.dump(temp, f)
