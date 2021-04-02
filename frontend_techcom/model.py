import numpy as np
import pymongo

class QueryMachine():
    def __init__(self, knn=None,url = None, tech_cate = None, com_cate = None):
        self.knn = knn
        self.url = url
        self.tech_cate = tech_cate
        self.com_cate = com_cate

    def update_data(self, knn=None,url = None,  tech_cate = None, com_cate = None):
        self.knn = knn
        self.tech_cate = tech_cate
        self.com_cate = com_cate
        self.url = url

    def search(self, src_name, model_index, k=5):
        print("src name", src_name)
        allnames = self.knn[model_index][src_name]
        names = []
        for name in allnames:
            if name in self.com_cate:
                names.append(name)
        names = names[:k]
        urls = []
        cates = []
        # for index, name in enumerate(names):
            # if name not in self.url:
                # name = name[:-(1+len(name.split()[-1]))]
                # names[index] = name
        urls = ['' for name in names] #[self.url[name] for name in names]
        cates = [self.com_cate[name] for name in names]
        return names, urls, cates

    def search_cate(self, src_name, model_index, cate, k=5):
        print("src name", src_name)
        allnames = self.knn[model_index][src_name]
        names = []
        for name in allnames:
            try:
                if cate in self.com_cate[name]:
                    names.append(name)
            except:
                continue
        names = names[:k]
        urls = []
        cates = []
        urls = ['' for name in names] #[self.url[name] for name in names]
        cates = [self.com_cate[name] for name in names]
        return names, urls, cates
    
    def get_src_cate(self, src_name):
        return self.tech_cate[src_name]
    
    
