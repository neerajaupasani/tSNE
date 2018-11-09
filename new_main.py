#import statements
import argparse
import new_protein
import skip_gram




def main():
    parser = argparse.ArgumentParser(description="Deepwalk")
    parser.add_argument('--input', default='protein.edges',help='Input graph path')

    parser.add_argument('--output',default='embeddings.csv',help='Embeddings')
    parser.add_argument('--representation-size', type=int, default=64)

    parser.add_argument('--walk-len', type=int, default=40)

    parser.add_argument('--num-walks', type=int, default=10)

    parser.add_argument('--window-size', type=int, default=5)

    parser.add_argument('--workers', type=int, default=1)

    args=parser.parse_args()



    processing(args)
#processing the algorithm
def processing(args):

    G=new_protein.Protein.load_graph(args.input,undirected=False)
    walks=new_protein.Protein.deep_walk(G,no_walks=args.num_walks,walk_length=args.walk_len)
    vertices=G.degree(nodes=None)
    model=skip_gram.Skipgram(sentences=walks,vocabulary=vertices,size=args.representation_size,window=args.window_size,workers=args.workers)
    model.wv.save_word2vec_format(args.output)

#load the main function to execute in the terminal as command-line arguments
if __name__ == "__main__":
    main()














