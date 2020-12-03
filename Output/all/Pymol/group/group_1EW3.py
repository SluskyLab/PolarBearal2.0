from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EW3.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 25-27 & chain A, resi 106-114 & chain A, resi 98-102 & chain A, resi 82-92 & chain A, resi 71-79 & chain A, resi 59-65 & chain A, resi 35-44 & chain A, resi 119-126 & chain A, resi 133-140 & chain A, resi 167-169 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[76.79391824382625,24.70328767332312,22.755876763226233])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
