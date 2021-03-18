import numpy as np
import pymongo

class QueryMachine():
    def __init__(self, knns=None, taxonomy = None):
        self.knns = knns
        self.taxonomy = taxonomy
    def update_data(self, knns=None, taxonomy = None):
        self.knns = knns
        self.process_tree(taxonomy) # for up down tree entity

    def process_tree(self, taxonomy):
        self.downent = taxonomy
        self.upent = {}
        for upent in self.downent:
            for ent in self.downent[upent]:
                if ent not in self.upent:
                    self.upent[ent] = []
                self.upent[ent].append(upent)
        self.upent = self.min_depth(self.upent)
        self.downent = self.max_depth(self.downent)

    
    def max_depth(self, tree):
        max_depth = {}
        for ent in tree:
            max = 0
            temp = tree[ent][0]
            for subent in tree[ent]:
                if int(subent.split('_')[-1]) > max:
                    max = int(subent.split('_')[-1])
                    temp = subent
            max_depth[ent[:-(len(ent.split('_')[-1])+1)]] = [temp[:-(len(temp.split('_')[-1])+1)]]
        return max_depth
    
    def min_depth(self, tree):
        max_depth = {}
        for ent in tree:
            max = 0
            temp = tree[ent][0]
            for subent in tree[ent]:
                if int(subent.split('_')[-1]) < max:
                    max = int(subent.split('_')[-1])
                    temp = subent
            max_depth[ent[:-(len(ent.split('_')[-1])+1)]] = [temp[:-(len(temp.split('_')[-1])+1)]]
        return max_depth
            
        

    def search(self, src_name, model_index,  k=5):
        print("src name", src_name)
        ents = self.knns[model_index][src_name][:k]
        print(src_name, ents)
        return ents
    
    
    def upsearch(self, src_name,model_index, k=5):
        ents = self.knns[model_index][src_name][:k]
        for index, ent in enumerate(ents):
            if ent in self.upent:
                print('okeeeeeeeeeeeeeeeeeeeeeee')
                ents[index] = self.upent[ent][0]
        return ents
    
    def downsearch(self, src_name,model_index, k=5):
        ents = self.knns[model_index][src_name][:k]
        for index, ent in enumerate(ents):
            if ent in self.downent:
                print('okeeeeeeeeeeeeeeeeeeeeeee')
                ents[index] = self.downent[ent][0]
        return ents
