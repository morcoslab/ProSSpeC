import sys
import pandas as pd
from Bio import SeqIO

"""

Takes in fasta file and ordered csv of Hamiltonian scores. Returns the best X items at output path

sys.argv[1] - path to fasta
sys.argv[2] - import path to csv
sys.argv[3] - int of top X to fetch
sys.argv[4] - path/name for output csv

"""

records = [record for record in SeqIO.parse(sys.argv[1], "fasta")]
ham_scores = pd.read_csv(sys.argv[2], header=None)
ham_scores = list(ham_scores.iloc[:,0])
data = zip(records,ham_scores)
data = sorted(data, key = lambda t: t[1])
# topX = data[0:int(sys.argv[3])]
topRecords, topHs = zip(*data)


file = open(sys.argv[4],"w")
for idx in range(0, len(records)):
    if idx == 0:
        file.write("ID, Full sequence, Protease sequence, Substrate sequence, Hamiltonian Specificity \n")
    full_seq = str(topRecords[idx].seq)
    file.write(topRecords[idx].description +","+full_seq+","+full_seq[0:-20]+","+full_seq[-20:]+","+str(topHs[idx])+"\n")
file.close()
