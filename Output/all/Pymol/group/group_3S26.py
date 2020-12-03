from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3S26.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 29-38 & chain A, resi 53-58 & chain A, resi 64-70 & chain A, resi 79-87 & chain A, resi 93-96 & chain A, resi 105-115 & chain A, resi 120-129 & chain A, resi 132-141 & chain A, resi 168-172 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[2.9513611257231482,-2.4093055404308767,-10.528944397707367])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
