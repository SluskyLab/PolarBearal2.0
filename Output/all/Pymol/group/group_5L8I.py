from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5L8I.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 5-13 & chain A, resi 37-44 & chain A, resi 47-54 & chain A, resi 59-65 & chain A, resi 118-126 & chain A, resi 108-115 & chain A, resi 98-104 & chain A, resi 90-95 & chain A, resi 80-87 & chain A, resi 69-72 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[45.695310901951146,-7.43510814099195,59.52972999778954])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
