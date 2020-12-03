from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ODD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 13-22 & chain A, resi 36-44 & chain A, resi 49-57 & chain A, resi 62-71 & chain A, resi 77-80 & chain A, resi 84-92 & chain A, resi 96-104 & chain A, resi 110-118 & chain A, resi 145-147 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-22.59191660086314,-2.511597224200765,-13.321013958917725])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
