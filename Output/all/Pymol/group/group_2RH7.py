from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2RH7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 11-22 & chain A, resi 25-36 & chain A, resi 41-50 & chain A, resi 118-127 & chain A, resi 104-113 & chain A, resi 91-99 & chain A, resi 172-183 & chain A, resi 156-167 & chain A, resi 140-143 & chain A, resi 146-153 & chain A, resi 194-204 & chain A, resi 213-221 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[22.375816770394643,-11.691449941694737,-14.488008403778077])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
