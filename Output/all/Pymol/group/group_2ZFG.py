from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZFG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-6 & chain A, resi 9-23 & chain A, resi 40-50 & chain A, resi 55-66 & chain A, resi 80-90 & chain A, resi 94-102 & chain A, resi 132-141 & chain A, resi 151-158 & chain A, resi 173-182 & chain A, resi 185-195 & chain A, resi 210-222 & chain A, resi 225-235 & chain A, resi 253-263 & chain A, resi 269-283 & chain A, resi 287-304 & chain A, resi 307-316 & chain A, resi 331-339 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-1.1589894040275819,44.965809463823916,-5.629290992211767])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 239-242 & chain A, resi 247-250 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-0.9295000303536654,44.4637508392334,-29.00987458229065])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
