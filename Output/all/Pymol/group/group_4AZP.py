from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AZP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 9-17 & chain A, resi 42-48 & chain A, resi 51-57 & chain A, resi 62-68 & chain A, resi 125-133 & chain A, resi 115-122 & chain A, resi 103-112 & chain A, resi 93-100 & chain A, resi 82-90 & chain A, resi 73-76 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[28.601746607430375,14.888240482139436,7.249898777826678])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
