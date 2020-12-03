from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5EZ2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 22-24 & chain A, resi 138-147 & chain A, resi 43-50 & chain A, resi 59-67 & chain A, resi 73-80 & chain A, resi 86-94 & chain A, resi 103-108 & chain A, resi 114-121 & chain A, resi 126-135 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[46.28219701202823,84.0124365578235,21.44591549080862])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
