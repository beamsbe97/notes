import numpy as np
import pandas as pd

class Node:
    def __init__(self, input_data):
        self.input_data = input_data
    
    def entropy(self):
        _, value_count = np.unique(self.input_data, return_counts=True)
        prob = value_count/len(self.input_data)
        entropy = 0
        for i in range(0, len(value_count)):
            entropy += prob[i]*np.log2(prob[i])
        return -entropy
    
    def avgChildEntropy(self, feature):
        num_of_nodes = len(np.unique(self.input_data[feature]))
        _, n_subnodes = np.unique(self.input_data[feature], return_counts=True)
        n_parent = len(self.input_data)
        avg_entroy = 0
        for i in range(0, num_of_nodes):
            avg_entroy+= n_subnodes[i]/n_parent
        return num_of_nodes
    
        
test = {"gender":[1,1,1,2,2],\
        "education":["Dip","Msc", "Bach", "Msc", "PhD"],\
        "job":["Tech", "Scientist", "Eng", "Scientist", "Scientist"]}

node1 = Node(test)
print(node1.avgChildEntropy("job"))