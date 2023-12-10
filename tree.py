import numpy as np
import pandas as pd

class Node:
    def __init__(self, input_data):
        self.input_data = input_data
    
    def entropy(self, predict_feature):
        _, value_count = np.unique(self.input_data[predict_feature], return_counts=True)
        prob = value_count/len(self.input_data)
        entropy = 0
        for i in range(0, len(value_count)):
            entropy += prob[i]*np.log2(prob[i])
        return -entropy
    
    def avgChildEntropy(self, feature):
        num_of_nodes = len(np.unique(self.input_data[feature]))
        unique_val, val_count = np.unique()
        n_parent = len(self.input_data)
        avg_entroy = 0
        for i in range(0, num_of_nodes):
            avg_entroy+= n_subnodes[i]/n_parent
        return num_of_nodes
    
    def getNodes(self, split_feature, predict_feature):
        num_of_nodes = len(np.unique(self.input_data[split_feature]))
        
        node1 = self.input_data[s]
        
        
test = {"gender":[1,1,1,2,2],\
        "education":["Dip","Msc", "Bach", "Msc", "PhD"],\
        "ethnicity":["A", "B", "A", "A", "B"],\
        "job":["Eng", "Scientist", "Eng", "Scientist", "Scientist"]}
dfTest = pd.DataFrame.from_dict(test)
node1 = Node(dfTest)
print(node1.avgChildEntropy("gender"))