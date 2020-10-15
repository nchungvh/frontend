import numpy as np
import pymongo

class QueryMachine():
    def __init__(self, results=None):
        self.results = results

    def update_data(self, results):
        self.results = results

    def search(self, src_type, src_name, target_type, k=5):
        print("src name", src_name)
        print(src_type, src_name, target_type)
        client = pymongo.MongoClient("mongodb://localhost:2710/")
        swiss_db = client["swiss"]
        graph_colect = swiss_db["graph"]
        indeed_collect = swiss_db["indeed_preprocess"]
        patent_collect = swiss_db["patent_preprocess"]
        raw_indeed_collect = swiss_db["indeed"]
        raw_patent_collect = swiss_db["patent"]
        if self.results is None:
            return ['Not init yet']
        try:
            if src_type == "Company":
                if target_type == "Company":
                    names = self.results['com_com'][src_name][:k]
                elif target_type == "Tech":
                    names =  self.results['com_tech'][src_name][:k]

            if src_type == "Tech":
                names = self.results['tech_com'][src_name][:k]
            indexs = [name.split('\t')[0] for name in names]
            id_sources = [graph_colect.find({'_id': str(index)})[0]['id_source'][0] for index in indexs]
            content_sources = [graph_colect.find({'_id': str(index)})[0]['content_detail'] for index in indexs]
            content_sources = [[i[0] for i in j] for j in content_sources]
            contents = []
            for index, idx in enumerate(id_sources):
                try:
                    fishing = patent_collect.find({'patent_id':idx})[0]
                    raw_names = [ent['rawName'] for ent in fishing['result']['entities']]
                    raw_name = [i for i in raw_names if i in content_sources[index]][0]
                    names[index] = raw_name
                    fishing_index = raw_names.index(raw_name)
                    start, end = fishing['result']['entities'][fishing_index]['offsetStart'], fishing['result']['entities'][fishing_index]['offsetEnd']
                    text = raw_patent_collect.find({'_id':idx})[0]
                    try:
                        text = text['abstract'][start-10, end+10]
                        contents.append(text)
                    except:
                        import pdb
                        pdb.set_trace()
                except:
                    fishing = indeed_collect.find({'id':idx})[0]
                    raw_names = [ent['rawName'] for ent in fishing['result']['entities']]
                    raw_name = [i for i in raw_names if i in content_sources[index]][0]
                    names[index] = raw_name
                    fishing_index = raw_names.index(raw_name)
                    start, end = fishing['result']['entities'][fishing_index]['offsetStart'], fishing['result']['entities'][fishing_index]['offsetEnd']
                    text = raw_indeed_collect.find({'_id':idx})[0]
                    try:
                        text = text['abstract'][start-10, end+10]
                        contents.append(text)
                    except:
                        import pdb
                        pdb.set_trace()
                
                return names, contents
            
        except:
            return []
