import pdb
import json
from collections import defaultdict

def get_meta_from_json(filepath):
    results = {}
    with open(filepath, 'r', encoding='utf-8') as f: 
        cnt = 0
        for line in f:
            if cnt == 0:
                results['com_com'] = json.loads(line)
            if cnt == 1:
                results['com_tech'] = json.loads(line)
            if cnt == 2:
                data = json.loads(line)
                d_dict = {}
                for k,v in data.items():
                    val = k.replace("_"," ").title()
                    d_dict[val] = v
                results['tech_com'] = d_dict
            cnt += 1
    n_dict = defaultdict(set)
    for k,v in results['com_com'].items():
        n_dict['company'].add(k)
    for k,v in results['tech_com'].items():
        val = k
        # val = k.replace("_", " ").lower()
        # val = k.replace("_"," ").title()
        n_dict['tech'].add(val)
    name_dict = {}
    name_dict['Company'] = sorted(list(n_dict['company']))
    name_dict['Tech'] = sorted(list(n_dict['tech']))
    return name_dict, results