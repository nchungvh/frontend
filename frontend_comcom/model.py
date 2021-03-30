import numpy as np
import pymongo

class QueryMachine():
    def __init__(self, knn=None,url = None, cate = None):
        self.knn = knn
        self.url = url
        self.cate = cate

    def update_data(self, knn=None,url = None, cate = None):
        self.knn = knn
        self.cate = cate
        self.url = url

    def search(self, src_name, model_index, k=5):
        print("src name", src_name)
        names = self.knn[model_index][src_name][:5]
        urls = []
        cates = []
        # for index, name in enumerate(names):
            # if name not in self.url:
                # name = name[:-(1+len(name.split()[-1]))]
                # names[index] = name
        urls = [self.url[name] for name in names]
        cates = [self.cate[name] for name in names]
        return names, urls, cates

    def search_cate(self, src_name, model_index, cate, k=5):
        print("src name", src_name)
        allnames = self.knn[model_index][src_name]
        names = [name for name in allnames if cate in self.cate[name]][:5]
        urls = []
        cates = []
        urls = [self.url[name] for name in names]
        cates = [self.cate[name] for name in names]
        return names, urls, cates
    
    def get_src_cate(self, src_name):
        return self.cate[src_name]
    
    
