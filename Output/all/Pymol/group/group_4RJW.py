from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RJW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 10-13 & chain A, resi 18-22 & chain A, resi 28-42 & chain A, resi 53-69 & chain A, resi 73-80 & chain A, resi 93-100 & chain A, resi 107-112 & chain A, resi 150-158 & chain A, resi 162-174 & chain A, resi 180-195 & chain A, resi 198-210 & chain A, resi 257-271 & chain A, resi 274-287 & chain A, resi 295-307 & chain A, resi 334-348 & chain A, resi 363-375 & chain A, resi 380-392 & chain A, resi 402-413 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[25.20878673977322,10.546248901188374,17.144359954396883])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
