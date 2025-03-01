from Bio import SeqIO
from random import randint

fasta = "full_tevp_msa.afa_filtered20"
data = [record for record in SeqIO.parse(fasta, "fasta")]
output = "shuffled_protease_and_autoinib_frag_filt20.fasta"
out_file = open(output,"w+")

for record in data:
    rand_idx = randint(0, len(data))
    protease = str(record.seq)[0:229]
    fragment = str(data[rand_idx].seq)[229:]
    shuffled_seq = protease + fragment
    out_file.write(">"+record.id+", "+ data[rand_idx].id+"\n"+ shuffled_seq+"\n")

out_file.close()
