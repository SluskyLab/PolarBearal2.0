from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QWD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 14-17 & chain A, resi 28-31 & chain A, resi 112-121 & chain A, resi 103-109 & chain A, resi 85-95 & chain A, resi 72-80 & chain A, resi 58-66 & chain A, resi 41-48 & chain A, resi 127-131 & chain A, resi 138-142 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[3.5732361879199743,32.30966726938883,35.21330584420098])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
