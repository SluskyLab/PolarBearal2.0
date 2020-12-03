from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GGE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-14 & chain A, resi 39-45 & chain A, resi 48-54 & chain A, resi 59-64 & chain A, resi 121-129 & chain A, resi 111-118 & chain A, resi 101-108 & chain A, resi 90-95 & chain A, resi 79-87 & chain A, resi 70-73 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-13.10705558458964,-16.131555583741928,-19.668305555979412])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
