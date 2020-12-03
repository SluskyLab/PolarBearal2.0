from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FGR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 3-17 & chain A, resi 26-31 & chain A, resi 320-331 & chain A, resi 286-297 & chain A, resi 269-281 & chain A, resi 253-264 & chain A, resi 235-249 & chain A, resi 218-230 & chain A, resi 199-213 & chain A, resi 183-196 & chain A, resi 171-179 & chain A, resi 148-155 & chain A, resi 137-141 & chain A, resi 86-90 & chain A, resi 76-83 & chain A, resi 51-60 & chain A, resi 38-48 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[23.760005528809593,57.44048082111963,3.306540990869204])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
