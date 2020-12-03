from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ALO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 34-43 & chain A, resi 53-58 & chain A, resi 62-70 & chain A, resi 48-50 & chain A, resi 75-84 & chain A, resi 92-97 & chain A, resi 100-110 & chain A, resi 115-124 & chain A, resi 128-142 & chain A, resi 165-169 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[2.197752959204509,3.31428233056384,1.4766823371105335])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
