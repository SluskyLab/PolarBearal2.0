from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EPA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 13-21 & chain A, resi 37-44 & chain A, resi 47-56 & chain A, resi 59-69 & chain A, resi 75-79 & chain A, resi 84-92 & chain A, resi 97-104 & chain A, resi 111-118 & chain A, resi 145-147 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-3.1596479040216394,11.133380294265882,10.063478920031601])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
