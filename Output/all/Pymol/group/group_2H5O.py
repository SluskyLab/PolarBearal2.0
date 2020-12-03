from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2H5O.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 12-22 & chain A, resi 25-35 & chain A, resi 41-50 & chain A, resi 117-127 & chain A, resi 104-114 & chain A, resi 91-99 & chain A, resi 172-183 & chain A, resi 156-167 & chain A, resi 140-143 & chain A, resi 146-153 & chain A, resi 193-204 & chain A, resi 210-220 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[1.1411885279612464,10.942877059466527,42.22331129918333])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
