import pdb
import json
from collections import defaultdict
import pandas

def get_knn(file_path):
    try:
        return json.load(open(file_path, 'r',encoding = 'utf-8'))
    except:
        return {}


def get_url_cate(file_path):
    # org = pandas.read_csv(file_path)
    # org = org[org['primary_role']=='company']
    # org = org[org['country_code']=='CHE']
    # cate = {}
    # url = {}
    # for index, line in org.iterrows():
    #     if line['name'] in cate:
    #         continue
    #     url[line['name']] = line['homepage_url']
    #     cate[line['name']] = line['category_groups_list']
    # for i in url:
    #     if pandas.isna(url[i]):
    #         url[i] = 'nothing'
    # for i in cate:
    #     if pandas.isna(cate[i]):
    #         cate[i] = 'nothing'
    #     cate[i] = cate[i].split(',')
    # return url, cate
    x = json.load(open(file_path))
    return x['url'], x['cate']


def get_taxonomy(file_path):
    # tree = ''
    tree = json.load(open(file_path, encoding = 'utf8'))
    return tree