import glob
import os
from pymol import cmd, stored
import csv


i = 0


# change the following to be the specific input and output of interest
POLARBEAREL_DIR="/Users/ryan/Desktop/gitLab/polarbearel/"
input_file ="%s/DB/AllDBList.txt"%(POLARBEAREL_DIR)
PyMOL_script_dir = "%s/Output/all/Pymol/B_strands/"%(POLARBEAREL_DIR)


pdb_list = []
with open(input_file) as f:
	for line in f.readlines():
		pdb_list.append(line[:5])
# remove header
#pdb_list = pdb_list[1:]
print(len(pdb_list)-1)
#print(pdb_list[0])

def load_next():
    global i
    i+=1
    if(i<len(pdb_list)):
        print("i=%s\tentry=%s"%(str(i),pdb_list[i]))
        show_chain_in_PDB(pdb_list[i])
    else:
        print("fin")
cmd.set_key('right', load_next)

def show_chain_in_PDB(entry):
    PDB = entry[:4]
    chain = entry[-1:]
    cmd.reinitialize('everything')
    cmd.set("bg_rgb", "white")
    cmd.run("%s/B_strands_%s.py"%(PyMOL_script_dir, PDB))
    cmd.show("cartoon", "all")
#    cmd.set('cartoon_color', "green")

    #cmd.fetch(PDB)
    #cmd.hide("everything", "all")
    #cmd.show("cartoon", "all")
    #cmd.color("green", PDB)

    #cmd.select("selected_chain", "chain %s"%(chain))
    #cmd.color("red", "selected_chain")
    #cmd.select("sele", "")
