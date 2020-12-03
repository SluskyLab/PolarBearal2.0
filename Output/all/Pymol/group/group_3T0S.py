from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3T0S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-22 & chain A, resi 30-43 & chain A, resi 51-64 & chain A, resi 87-101 & chain A, resi 104-111 & chain A, resi 129-137 & chain A, resi 143-154 & chain A, resi 178-186 & chain A, resi 191-200 & chain A, resi 204-216 & chain A, resi 221-234 & chain A, resi 244-256 & chain A, resi 259-269 & chain A, resi 300-309 & chain A, resi 318-330 & chain A, resi 339-351 & chain A, resi 361-371 & chain A, resi 376-390 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[21.141640918905086,-21.175099929625336,-7.60635450696996])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
