import pdb
import json
from collections import defaultdict
import pandas

def get_knn(file_path):
    try:
        knn = json.load(open(file_path, 'r',encoding = 'utf-8'))
        for key in knn:
            knn[key] = [i[0] for i in knn[key]]
        return knn
    except:
        return {}


def get_tech_cate(file_path, knn):
    org = pandas.read_csv(file_path)
    cate = {}
    url = {}
    for index, line in org.iterrows():
        if line['name'] in cate:
            continue
        # url[line['name']] = line['homepage_url']
        cate[line['name']] = line['category_groups_list']
    for i in url:
        if pandas.isna(url[i]):
            url[i] = 'nothing'
    for i in cate:
        if pandas.isna(cate[i]):
            cate[i] = 'nothing'
        cate[i] = cate[i].split(',')
    
    tech_cate = {}
    tech_url = {}
    for tech in knn:
        list_cate = []
        for com in knn[tech]:
            try:
                list_cate.extend(cate[com])
            except:
                continue
        list_cate = list(set(list_cate))
        tech_cate[tech] = list_cate
        tech_url[tech] = ''
    return tech_url, tech_cate, cate


def get_taxonomy(file_path):
    # tree = ''
    tree = json.load(open(file_path, encoding = 'utf8'))
    return tree