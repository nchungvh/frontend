import numpy as np


class QueryMachine():
    def __init__(self, results=None):
        self.results = results

    def update_data(self, results):
        self.results = results

    def search(self, src_type, src_name, target_type, k=5):
        print("src name", src_name)
        print(src_type, src_name, target_type)
        if self.results is None:
            return ['Not init yet']
        try:
            if src_type == "Company":
                if target_type == "Company":
                    return self.results['com_com'][src_name][:k]
                elif target_type == "Tech":
                    return self.results['com_tech'][src_name][:k]

            if src_type == "Tech":
                return self.results['tech_com'][src_name][:k]
        except:
            return []
