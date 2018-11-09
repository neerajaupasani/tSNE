#import statements
import pandas as pd
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#loading the csv file from embeddings.csv into new_embeddings.csv with the data split into columns
data=pd.read_csv("C:/Users/Admin/PycharmProjects/protein_edgelist/new_embeddings.csv")

#slicing the embeddings of the nodes
dimensions=data.iloc[:,1:64]

#embedding in 2D space
model=TSNE(n_components=2,random_state=0)

#fitting the model
tsne_data=model.fit_transform(dimensions)

#plotting the embeddings
plt.plot(dimensions)
plt.show()






#tsne_data=np.vstack((tsne_data.T,nodes)).T
#tsne_df=pd.DataFrame(data=tsne_data,columns=("Dim1","Dim2","Nodes"))

#sns.FacetGrid(tsne_data,hue="Nodes",size=6).map(plt.scatter,'Dim1','Dim2','Nodes')



