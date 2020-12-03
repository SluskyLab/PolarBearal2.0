from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WWP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 41-50 & chain A, resi 65-71 & chain A, resi 77-85 & chain A, resi 88-98 & chain A, resi 104-109 & chain A, resi 114-123 & chain A, resi 128-137 & chain A, resi 144-150 & chain A, resi 177-179 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[16.613573395411173,-10.976013314723968,4.938879994675517])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
