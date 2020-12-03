from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X9K.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-21 & chain A, resi 24-39 & chain A, resi 43-54 & chain A, resi 65-79 & chain A, resi 83-97 & chain A, resi 106-121 & chain A, resi 126-138 & chain A, resi 149-160 & chain A, resi 166-177 & chain A, resi 188-196 & chain A, resi 204-218 & chain A, resi 233-243 & chain A, resi 248-259 & chain A, resi 268-279 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[0.23277294650875233,-15.377075639427513,21.190929724719073])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
