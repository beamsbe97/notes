import pandas as pd
import numpy as np

df = {"Outlook":['R','R','O','S','S','S','O','R','R','S','R','O','O','S'],
     "Temp":    ['H','H','H','M','C','C','C','M','C','M','M','M','H','M'],
     "Humidity":['H','H','H','H','N','N','N','H','N','N','N','H','N','H'],
     "Windy"   :['f','t','f','f','f','t','t','f','f','f','t','t','f','t'],
     "Play"    :['n','n','y','y','y','n','y','n','y','y','y','y','y','n']}
df = pd.DataFrame.from_dict(df)

class bayes():
    def __init__(self, X, y_feature):
        self.X = X
        self.y_feature = y_feature
        self.y_classes, self.y_counts = np.unique(X[y_feature], return_counts=True)
        self.features = X.columns
        self.y_probs = self.y_counts/len(X)
        

    def classify(self, x : list[str]) -> str: #takes in combi of weather values, returns play
        p_yx = 0
        selected_y = ''

        for asd in range(0,len(self.y_classes)):
            likelihood=1
            x_probs=1
            y1 = self.X[self.X[self.y_feature] == self.y_classes[asd]]
            for i in range(0, len(x)):
                likelihood*= (len(y1[y1[self.features[i]]==x[i]])/self.y_counts[asd])  

                x_probs*= (len(self.X[self.X[self.features[i]]==x[i]])/len(self.X))

            post_y = (likelihood*self.y_probs[asd])/x_probs

            if post_y > p_yx:
                p_yx = post_y
                selected_y = self.y_classes[asd]
        
        return selected_y 

model = bayes(df, "Play")
model.classify(['R', 'M', 'N', 't'])