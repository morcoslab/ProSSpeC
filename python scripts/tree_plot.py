from ete3 import NCBITaxa, Tree, faces, AttrFace, TreeStyle, NodeStyle, CircleFace
from Bio import SeqIO
import requests
import numpy as np
import pickle as pkl 
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt


def layout(node):
    if not node.is_leaf():
        N = AttrFace("sci_name", fsize=14, fgcolor="black")
        N.rotation = 0
        faces.add_face_to_node(N, node, 0, position="branch-top")
    if node.is_leaf():
        # Add node name to laef nodes
        N = AttrFace("sci_name", fsize=14, fgcolor="black")
        N.rotation = 0
        faces.add_face_to_node(N, node, 0)
        W = AttrFace("weight", fsize=12, fgcolor="black", text_prefix="( ", text_suffix=" )")
        W.rotation =0
        faces.add_face_to_node(W, node, 0)
    # if "weight" in node.features:
        # Creates a sphere face whose size is proportional to node's
        # feature "weight"
        # NS = NodeStyle()
        # NS["bgcolor"] = mpl.colors.rgb2hex(m.to_rgba(n.weight), keep_alpha=True)
        # n.set_style(NS)

uniprot_ids = [record.id for record in SeqIO.parse("concat_seqs_peptidaseC4.fasta",'fasta')]

potyviridae_taxid = 39729
genus_ids = [2733284,2169648,675844,39731,2733285,137757,156208,1230390,12195,39730,2169649,156207]
genus_ids.append(potyviridae_taxid)
genus_names = ["Arepavirus", "Bevemovirus","Brambyvirus","Bymovirus", "Celavirus", "Ipomovirus", "Macluravirus", "Poacevirus", "Potyvirus", 
                "Rymovirus", "Roymovirus", "Tritimovirus"]
ncbi = NCBITaxa()
tree = ncbi.get_topology(genus_ids,)

file = open("/home/ceziegler/Documents/NIA_files/training_data_genus_counts.pkl","rb")
lineage_counts = pkl.load(file)
lineage_count_lbl = [str(int(num)) for num in lineage_counts]
file.close()

# get tax ids for all proteins used in training
# lineage_counts = np.zeros(len(genus_names))
# failed=[]
# for id in uniprot_ids:
#     try:
#         r = requests.get("https://rest.uniprot.org/uniprotkb/"+id+".json")
#         tax = r.json()["organism"]["lineage"]
#         genus_idxs = [genus_names.index(item) for item in tax if item in genus_names]
#         lineage_counts[genus_idxs[0]] += 1
#     except:
#         failed.append(id)

norm = mpl.colors.Normalize(vmin=min(lineage_counts), vmax=max(lineage_counts))
cmap = cm.Blues
m = cm.ScalarMappable(norm=norm, cmap=cmap)

for n in tree.traverse():
    if n.sci_name in genus_names:
        n.add_features(weight=str(int(lineage_counts[genus_names.index(n.sci_name)])))

genus_names.append("Unclassified")

for n in tree.traverse():
    if n.name == "39729":
        unknown = n.add_child(name="Unclassified")
        unknown.add_features(weight=lineage_count_lbl[-1], rank="genus",sci_name="Unclassified")     

for n in tree.traverse():
    if n.sci_name in genus_names:
        n.add_features(weight=int(lineage_counts[genus_names.index(n.sci_name)])) 
        NS = NodeStyle()
        NS["size"] = 4
        NS["vt_line_width"] = 5
        NS["hz_line_width"] = 4
        NS["vt_line_type"] = 0 # 0 solid, 1 dashed, 2 dotted
        NS["hz_line_type"] = 0
        if n.weight == 0:
            NS["vt_line_type"] = 1 # 0 solid, 1 dashed, 2 dotted
            NS["hz_line_type"] = 1
        NS["bgcolor"] = mpl.colors.rgb2hex(m.to_rgba(n.weight))
        n.set_style(NS)
        

ts = TreeStyle()
ts.layout_fn = layout
ts.mode = "c"
ts.show_leaf_name = False
ts.rotation = 0  # This ensures the entire tree starts at 0 degrees  # This prevents label rotation
tree.show(tree_style=ts)

# fig, ax = plt.subplots()   
# cbar = plt.colorbar(m, ax=ax, label="Number of training sequences")
# cbar.solids.set_edgecolor("face")
# plt.show()
