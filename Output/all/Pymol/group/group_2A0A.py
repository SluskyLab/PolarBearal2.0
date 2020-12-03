from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2A0A.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-10 & chain A, resi 39-44 & chain A, resi 49-53 & chain A, resi 60-64 & chain A, resi 123-130 & chain A, resi 112-118 & chain A, resi 102-108 & chain A, resi 91-96 & chain A, resi 78-87 & chain A, resi 70-74 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-0.07576561346650124,-1.6677656422834843,-2.081421883427538])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
