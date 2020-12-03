from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2O62.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 13-22 & chain A, resi 28-41 & chain A, resi 46-53 & chain A, resi 59-63 & chain A, resi 116-126 & chain A, resi 102-110 & chain A, resi 92-99 & chain A, resi 78-80 & chain A, resi 70-72 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[14.687266590197881,19.736840031941732,31.83635986328125])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 144-154 & chain A, resi 161-171 & chain A, resi 177-183 & chain A, resi 186-195 & chain A, resi 198-201 & chain A, resi 209-213 & chain A, resi 218-223 & chain A, resi 232-241 & chain A, resi 244-252 & chain A, resi 258-268 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-0.018402313727928304,4.39619539506819,25.605907977312462])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
