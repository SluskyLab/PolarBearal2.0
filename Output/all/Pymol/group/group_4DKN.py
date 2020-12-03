from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4DKN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-15 & chain A, resi 18-28 & chain A, resi 35-41 & chain A, resi 110-120 & chain A, resi 97-107 & chain A, resi 84-92 & chain A, resi 166-177 & chain A, resi 150-161 & chain A, resi 133-136 & chain A, resi 139-146 & chain A, resi 191-201 & chain A, resi 205-215 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[4.176068361498352,-13.264700792220413,-13.339196603203941])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
