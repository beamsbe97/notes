import numpy as np
import pandas as pd
class Tree():
    def __init__(self, X, predict_feature):
        self.X = X
        self.predict_feature = predict_feature
        self.output_classes = np.unique(X[predict_feature])
        self.features = list(self.X.columns)
        self.features.remove(predict_feature)
        
class Node(Tree):
    def __init__(self, X, predict_feature):
        super().__init__(X, predict_feature)
        self.node_entropy = self.entropy(X)
        
    def entropy(self, input_data):
        _, value_count = np.unique(input_data[self.predict_feature], return_counts=True)
        prob = value_count/len(input_data)
        entropy = 0
        for i in range(0, len(value_count)):
            entropy += prob[i]*np.log2(prob[i])
        return -entropy
    
    def avgChildEntropy(self, feature):
        split_classes = np.unique(self.X[feature])
        nodes = []
        for i in range(0, len(split_classes)):
            nodes.append(self.X[self.X[feature]==split_classes[i]])
        #node1 = self.X[self.X[feature]==split_classes[0]]
        #node2 = self.X[self.X[feature]==split_classes[1]]
        
        n_parent = len(self.X)
        
        n_subnodes = []
        for i in range(0, len(nodes)):
            n_subnodes.append(len(nodes[i]))
        
        
        
        n_subnode1 = len(node1[node1[self.predict_feature] == self.output_classes[0]])
        n_subnode2 = len(node2[node2[self.predict_feature] == self.output_classes[1]])
       
        entropy_node1 = self.entropy(node1)
        entropy_node2 = self.entropy(node2)
        
        avg_entropy = 0
        
        for i in range(0, len(split_classes)):
            avg_entropy+= len
        
        avg_entropy = (n_subnode1/n_parent)*entropy_node1 +(n_subnode2/n_parent)*entropy_node2
        
        return avg_entropy
    
    def infoGain(self, feature):
        return self.node_entropy - self.avgChildEntropy(feature)
    
    def splitSelect(self):
        highest_gain = 0
        selected_feature = ""
        for feature in self.features:
            if self.infoGain(feature) > highest_gain:
                highest_gain = self.infoGain(feature)
                selected_feature = feature
        return selected_feature, highest_gain   
        
test = {"gender":[1,1,1,2,2],\
        "education":["Dip","Msc", "Bach", "Msc", "PhD"],\
        "ethnicity":["A", "B", "A", "A", "B"],\
        "job":["Eng", "Scientist", "Eng", "Scientist", "Scientist"]}

student = {
    "exam":['P','F','F','P','F','F','P','P','P','P','P','P','F','F','F'],\
    "other_courses":['Y','N','Y','Y','N','Y','Y','Y','N','N','Y','N','Y','N','N'],\
    "background":["Maths","Maths","Maths","CS","Other","Other","Maths","CS","Maths","CS","CS","Maths","Other","Other","Maths"],\
    "work_status":["NW","W","W","NW","W","W","NW","NW","W","W","W","NW","W","NW","W"]
}
len(student["work_status"])
dfTest = pd.DataFrame.from_dict(test)

node1 = Node(dfTest, "job")

node1_entropy = node1.entropy(node1.X)
gender_avg_entropy = node1.avgChildEntropy("gender")

print(node1.output_classes)
print(node1.predict_feature)

print(gender_avg_entropy)

node1.features

print(node1.splitSelect())

n = [1,2,3]
m = [3,4,5]

test = [a*b for a,b in zip(n,m)]



