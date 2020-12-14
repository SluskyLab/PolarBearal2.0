from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PHO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 10-24 & chain A, resi 40-49 & chain A, resi 55-66 & chain A, resi 79-90 & chain A, resi 94-102 & chain A, resi 132-142 & chain A, resi 151-158 & chain A, resi 173-182 & chain A, resi 185-195 & chain A, resi 210-222 & chain A, resi 225-235 & chain A, resi 253-263 & chain A, resi 269-281 & chain A, resi 290-302 & chain A, resi 307-316 & chain A, resi 331-339 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[0.5731854004304061,46.310612367780024,31.080702160181623])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
