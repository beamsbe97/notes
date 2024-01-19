import numpy as np
import pandas as pd
class Tree():
    def __init__(self, X, predict_feature):
        self.X = X
        self.predict_feature = predict_feature
        self.output_classes, self.class_count = np.unique(X[predict_feature], return_counts=True)
        self.features = list(self.X.columns)
        self.features.remove(predict_feature)
        
class Node(Tree):
    def __init__(self, X, predict_feature):
        super().__init__(X, predict_feature)
        self.node_entropy = self.entropy(X)

    def isLeaf(self):
        return len(np.unique(self.X[self.predict_feature])) == 1
        
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
        
        n_parent = len(self.X)
        avg_entropy = 0
        for i in range(0, len(nodes)):
            avg_entropy+= (len(nodes[i])/n_parent)*self.entropy(nodes[i])
        
        return avg_entropy
    
    def infoGain(self, feature):
        return self.node_entropy - self.avgChildEntropy(feature)
    
    def indi_gini(self, node): #pass in child data
        node_gini = 1
        for i in range(0, len(self.output_classes)):
            node_gini-=(len(node[node[self.predict_feature]==self.output_classes[i]])/len(node))**2
        return node_gini
    
    def overall_gini(self, feature): #parent
        split_classes = np.unique(self.X[feature])
        overall_gini = 0
        for i in range(0, len(split_classes)):
            overall_gini += (len(self.X[self.X[feature]==split_classes[i]])/len(self.X))*self.indi_gini(self.X[self.X[feature]==split_classes[i]])
        return overall_gini    
  
    def split_select_gini(self): #returns feature with lowest gini index
        lowest_gini = 0
        self.selected_feature = ""
        for feature in self.features:
            if self.overall_gini(feature) < lowest_gini:
                lowest_gini = self.overall_gini(feature)
                self.selected_feature = feature
        return self.selected_feature, lowest_gini
    
    def split_select_infoGain(self):
        highest_gain = 0
        self.selected_feature = ""
        for feature in self.features:
            if self.infoGain(feature) > highest_gain:
                highest_gain = self.infoGain(feature)
                self.selected_feature = feature
        return self.selected_feature, highest_gain  

    def split(self, split_by): 
        split_list= {} #each element is a node after splitting
        split_values = np.unique(self.X[split_by])
        for i in range(0, len(split_values)):
            node = pd.DataFrame(self.X[self.X[split_by]==split_values[i]])
            node = node.drop(columns=[split_by])
            split_list[split_values[i]] = node
            #split_list.append(node)
        return split_list

def leafClassifer(data, labelCol): 
    classes, n_classes = np.unique(data[labelCol], return_counts=True)

    return classes[n_classes.argmax()] #returns most frequent output class


def decision_tree(data, labelCol, min_split):
    node = Node(data,labelCol)
    if node.isLeaf() or len(node.X) < min_split or len(node.X.columns)==1: #default value for recursion
        return leafClassifer(data, labelCol)
    else:
        node.split_select_infoGain()
        split_nodes = node.split(node.selected_feature)
        myTree = {node.selected_feature:{}}
        
        for subnode_name, subnode_data in split_nodes.items():
            myTree[node.selected_feature][subnode_name] = decision_tree(subnode_data,labelCol, min_split)
        return myTree


def predict(input_row, input_tree):
    split_column = list(input_tree.keys())[0]
    for key,value in input_tree[split_column].items():
        if input_row[split_column] == key:
            if type(value).__name__ == 'str':
                return value
            else:
                return predict(input_row, input_tree[split_column][key])



student = {
    "exam":['P','F','F','P','F','F','P','P','P','P','P','P','F','F','F'],\
    "other_courses":['Y','N','Y','Y','N','Y','Y','Y','N','N','Y','N','Y','N','N'],\
    "background":["Maths","Maths","Maths","CS","Other","Other","Maths","CS","Maths","CS","CS","Maths","Other","Other","Maths"],\
    "work_status":["NW","W","W","NW","W","W","NW","NW","W","W","W","NW","W","NW","W"]
}

testVec = {
    "exam":['P'],\
    "other_courses":['N'],\
    "background":["Maths"],\
    "work_status":["NW"]
}
testVec = pd.DataFrame.from_dict(testVec)

len(student["work_status"])
dfTest = pd.DataFrame.from_dict(student)

node1 = Node(dfTest, "exam")

tree = decision_tree(dfTest,"exam", 2)

testVec["predicted"] = testVec.apply(predict, args=(tree),axis=1)

def testfun(x):
    return x["exam"]+x["background"]

dfTest.apply(testfun, axis=1)




