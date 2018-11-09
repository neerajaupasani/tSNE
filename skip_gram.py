# import statements
from collections import defaultdict
from gensim.models import Word2Vec

#skipgram model for deepwalk to get the output of the representation in skipgram format.For the deepwalk algorithm the
#sentences are the walks and the vocabulary is the number of nodes.

class Skipgram(Word2Vec):

    def __init__(self,vocabulary=None,**kwargs):

        self.vocabulary=None
        #kwargs["min_count"] = kwargs.get("min_count", 0)
        kwargs["workers"] = kwargs.get("workers",1)
        kwargs["size"] = kwargs.get("size",64)
        kwargs["sentences"] = kwargs.get("sentences", None)
        kwargs["window"] = kwargs.get("window", 5)
        #kwargs["sg"] = 1
        #kwargs["hs"] = 1

        if vocabulary != None:
            self.vocabulary = vocabulary
            super(Skipgram, self).__init__(**kwargs)




        


