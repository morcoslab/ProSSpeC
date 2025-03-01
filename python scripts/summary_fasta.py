import pandas as pd
from Bio import SeqIO
import numpy as np
"""
Makes a summary table for all the organisms and variants in the training fasta
"""

concat_fasta = "concat_seqs_peptidaseC4.fasta"
protease_fasta = "peptidaseC4_all_filtered45.fasta"

ids =[record.id for record in SeqIO.parse(concat_fasta, "fasta")]
orgs = [record.description.split("OS=")[1].split(" OX=")[0].split("(")[0] for record in SeqIO.parse(protease_fasta, "fasta")]
protease_ids = [record.id.split("|")[1] for record in SeqIO.parse(protease_fasta, "fasta")]

unique_orgs = list(set(orgs))
unique_org_count = np.zeros(len(unique_orgs))
for accession in ids:
    org_idx = protease_ids.index(accession)
    unique_org_count[unique_orgs.index(orgs[org_idx])] += 1

results = pd.DataFrame({"Organism": unique_orgs, "Number of Variants": unique_org_count})
results = results.loc[(results["Number of Variants"]!=0)]
results.to_csv("training_data_unique_org_count.csv")
