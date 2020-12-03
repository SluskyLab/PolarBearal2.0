from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4HE4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 12-22 & chain A, resi 25-36 & chain A, resi 41-48 & chain A, resi 116-126 & chain A, resi 103-113 & chain A, resi 90-98 & chain A, resi 176-187 & chain A, resi 158-168 & chain A, resi 146-153 & chain A, resi 199-208 & chain A, resi 217-227 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[17.436104262393453,15.664408730423968,14.09114786185648])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
