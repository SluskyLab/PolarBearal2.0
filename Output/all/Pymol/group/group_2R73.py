from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2R73.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 29-35 & chain A, resi 121-130 & chain A, resi 109-118 & chain A, resi 96-102 & chain A, resi 88-92 & chain A, resi 72-82 & chain A, resi 60-69 & chain A, resi 50-57 & chain A, resi 157-159 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[4.64146480116416,65.97663395841357,23.931281613631988])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
