from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3P6D.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-14 & chain A, resi 39-45 & chain A, resi 48-54 & chain A, resi 60-64 & chain A, resi 122-130 & chain A, resi 112-119 & chain A, resi 100-109 & chain A, resi 90-97 & chain A, resi 79-87 & chain A, resi 70-73 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[8.833083330237839,10.587869042663701,13.08172621755373])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
