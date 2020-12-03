from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FIQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 14-23 & chain A, resi 38-44 & chain A, resi 50-59 & chain A, resi 62-72 & chain A, resi 78-81 & chain A, resi 85-93 & chain A, resi 97-105 & chain A, resi 111-119 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[7.054614297513451,-7.267271412722766,-30.95544297354562])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
