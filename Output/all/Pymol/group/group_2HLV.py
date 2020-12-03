from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HLV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 18-24 & chain A, resi 112-120 & chain A, resi 98-106 & chain A, resi 86-94 & chain A, resi 79-82 & chain A, resi 63-73 & chain A, resi 51-60 & chain A, resi 39-46 & chain A, resi 146-148 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[22.111014311654227,43.30197170802525,5.746542860128518])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
