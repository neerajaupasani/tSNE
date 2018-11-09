#import statements
import numpy as np
from collections import defaultdict
from collections import Iterable




#defining the class and constructor for the class
class Protein(defaultdict):
    def __init__(self):
        super(Protein, self).__init__(list)

#number of nodes in the graph
    def degree(self, nodes=None):
        if isinstance(nodes, Iterable):
            return {v: len(self[v]) for v in nodes}
        else:
            return len(self[nodes])

#load the edges file
    def load_graph(self,undirected=False):
        G=Protein()
        with open("protein.edges",'r') as f:
            for l in f:
                x, y = l.strip().split()[:2]
                x = int(x)
                y = int(y)
                G[x].append(y)
                if undirected:
                    G[y].append(x)
        return G


#deepwalk algorithm->random walk generator
    def deep_walk(self,no_walks,walk_length):
        G=self
        walks = list()
        # random sampling of the nodes
        for start_node in list(G.keys()):
            for i in range(no_walks):
                path = [start_node]
                path_list = list(G[start_node])
                if len(path_list) == 0:
                    break
                first_node = np.random.choice(path_list)
                path.append(first_node)
                #random sampling from the neighbours of last vertex
                for k in range(walk_length):
                    path_list = list(G[path[-1]])
                    if len(path_list) == 0:
                        break
                    neighbour = np.random.choice(path_list)
                    path.append(neighbour)
                walks.append(path)
        np.random.shuffle(walks)
        walks = [list(map(str,walk)) for walk in walks]
        return walks




