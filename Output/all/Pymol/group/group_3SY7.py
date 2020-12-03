from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SY7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 18-51 & chain A, resi 60-75 & chain A, resi 96-108 & chain A, resi 111-118 & chain A, resi 137-144 & chain A, resi 150-174 & chain A, resi 179-194 & chain A, resi 197-206 & chain A, resi 210-224 & chain A, resi 227-240 & chain A, resi 250-262 & chain A, resi 265-276 & chain A, resi 283-285 & chain A, resi 314-323 & chain A, resi 332-344 & chain A, resi 365-377 & chain A, resi 387-397 & chain A, resi 406-416 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[27.42062718512719,-12.675157926388477,13.650947342698233])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
