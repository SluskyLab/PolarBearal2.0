from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3BRY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 43-59 & chain A, resi 80-91 & chain A, resi 94-103 & chain A, resi 130-145 & chain A, resi 150-169 & chain A, resi 200-203 & chain A, resi 214-230 & chain A, resi 233-240 & chain A, resi 248-252 & chain A, resi 268-273 & chain A, resi 280-288 & chain A, resi 293-302 & chain A, resi 310-315 & chain A, resi 327-329 & chain A, resi 335-347 & chain A, resi 350-360 & chain A, resi 378-387 & chain A, resi 392-401 & chain A, resi 420-435 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[48.981029548081274,-11.039448307891345,-58.68670930533573])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
