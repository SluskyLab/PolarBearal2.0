from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1E5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-19 & chain B, resi 35-39 & chain B, resi 44-53 & chain B, resi 30-32 & chain B, resi 56-67 & chain B, resi 71-76 & chain B, resi 79-83 & chain B, resi 91-100 & chain B, resi 86-88 & chain B, resi 105-113 & chain B, resi 140-142 & chain B, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-41.549784889704064,58.47322787514216,22.1242784367332])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
